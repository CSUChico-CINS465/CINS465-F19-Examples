from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,page=0):
    value=range(10*page+10)
    context={
        "variable":"Hello World",
        "title":"Index",
        "some_list":value[page*9:(page*9+9)]
    }
    return render(request, "index.html", context=context)
