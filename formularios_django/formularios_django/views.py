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
    if request.method == "GET":
        form=ContactForm()
        return render(request,"widget.html",{"form":form})
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # acciones a realizar cuando lo datos son correctos
            return HttpResponse("Valido")
        else:
            # acciones cuando los datos no sean correctos
            return render(request,"widget.html",{"form":form})


    