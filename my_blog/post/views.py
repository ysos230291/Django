from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Jesus"
    author.email = "jesuscabrera230291@gmail.com"
    author.save()
    return HttpResponse("Actualizado")


def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.filter(name__contains="father")

    # obtener datos filtrados por condicion
    filtred = Author.objects.filter(id__lte=15)

    # obtener un unico objeto
    author = Author.objects.get(id=1)

    return render(request,'post/queries.html',{'authors':authors, 'filtred':filtred, 'author':author})

