from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import models
from . import forms

# Create your views here.
def index(request,page=0):
    if request.method=="POST":
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            new_sugg = models.Suggestion(suggestion=form_instance.cleaned_data["suggestion"])
            new_sugg.save()
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
            suggestion_list["suggestions"] += [{"suggestion":s_q.suggestion}]
        return JsonResponse(suggestion_list)
    else:
        return HttpResponse("Unsupported HTTP Method")

def logout_view(request):
    logout(request)
    return redirect("/login/")