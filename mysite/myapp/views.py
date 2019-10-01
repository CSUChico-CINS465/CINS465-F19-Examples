from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

from . import models
from . import forms

# Create your views here.
def index(request,page=0):
    if request.method=="POST":
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
    value=models.Suggestion.objects.all()
    context={
        "variable":"Hello World",
        "title":"Index",
        "form":form_instance,
        "some_list":value
    }
    return render(request, "index.html", context=context)

@csrf_exempt
@login_required(login_url='/login/')
def suggestions_view(request):
    if request.method == "GET":
        suggestion_query=models.Suggestion.objects.all()
        suggestion_list = {"suggestions":[]}
        for s_q in suggestion_query:
            suggestion_list["suggestions"] += [{
                "suggestion":s_q.suggestion,
                "author":s_q.author.username
                }]
        return JsonResponse(suggestion_list)
    else:
        return HttpResponse("Unsupported HTTP Method")

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
