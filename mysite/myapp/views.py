from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# from django.contrib.auth.models import User

from . import models
from . import forms

# Create your views here.
def index(request, page=0):
    if request.method == "POST":
        if request.user.is_authenticated:
            form_instance = forms.SuggestionForm(request.POST)
            if form_instance.is_valid():
                new_sugg = models.Suggestion(suggestion=form_instance.cleaned_data["suggestion"])
                new_sugg.author = request.user
                new_sugg.save()
                form_instance = forms.SuggestionForm()
        else:
            form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()
    suggestion_query = models.Suggestion.objects.all()
    suggestion_list = {"suggestions":[]}
    for s_q in suggestion_query:
        comment_query = models.Comment.objects.filter(suggestion=s_q)
        comment_list = []
        for c_q in comment_query:
            can_delete=False
            if request.user == c_q.author:
                can_delete=True
            comment_list += [{
            "comment":c_q.comment,
            "author":c_q.author.username,
            "created_on":c_q.created_on,
            "id":c_q.id,
            "delete":can_delete
            }]
        suggestion_list["suggestions"] += [{
            "id":s_q.id,
            "suggestion":s_q.suggestion,
            "author":s_q.author.username,
            "created_on":s_q.created_on,
            "comments":comment_list
            }]
    context = {
        "variable":"Hello World",
        "title":"Index",
        "form":form_instance,
        "some_list":suggestion_list["suggestions"]
    }
    return render(request, "index.html", context=context)

@csrf_exempt
@login_required(login_url='/login/')
def suggestions_view(request):
    if request.method == "GET":
        suggestion_query = models.Suggestion.objects.all()
        suggestion_list = {"suggestions":[]}
        for s_q in suggestion_query:
            comment_query = models.Comment.objects.filter(suggestion=s_q)
            comment_list = []
            for c_q in comment_query:
                can_delete=False
                if request.user == c_q.author:
                    can_delete=True
                comment_list += [{
                "comment":c_q.comment,
                "author":c_q.author.username,
                "created_on":c_q.created_on,
                "id":c_q.id,
                "delete":can_delete
                }]
            suggestion_list["suggestions"] += [{
                "id":s_q.id,
                "suggestion":s_q.suggestion,
                "author":s_q.author.username,
                "created_on":s_q.created_on,
                "comments":comment_list
                }]
        return JsonResponse(suggestion_list)
    return HttpResponse("Unsupported HTTP Method")

@login_required(login_url='/login/')
def comments_view(request, instance_id, delete=0):
    if delete==1:
        print("Should delete the comment here")
        instance = models.Comment.objects.get(id=instance_id)
        if request.user == instance.author:
            instance.delete()
        return redirect("/")
    if request.method == "POST":
        if request.user.is_authenticated:
            form_instance = forms.CommentForm(request.POST)
            if form_instance.is_valid():
                new_comm = form_instance.save(request=request, sugg_id=instance_id)
                return redirect("/")
        else:
            form_instance = forms.CommentForm()
    else:
        form_instance = forms.CommentForm()
    context = {
        "title":"Comment Form",
        "form":form_instance,
        "sugg_id":instance_id
    }
    return render(request, "comment.html", context=context)


def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
            # print("Hi")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)
