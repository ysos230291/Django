from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommenntForm, ContactForm

def form(request):
    comment_form=CommenntForm()
    return render(request,"form.html",{"comment_form":comment_form})

def goal(request):
    if request.method != "GET":
        return HttpResponse("Metodo no permitido")

    return HttpResponse(request.GET["name"])

def widget(request):
    form=ContactForm()
    return render(request,"widget.html",{"form":form})


    