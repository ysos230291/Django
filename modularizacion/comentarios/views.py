from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Pincha al kilo")

def create(request):
    #comment = Comment(name = "Juanjo", score = 5, comment = "Este es un comentario")
    #comment.save()      ---->> de esta manera puedes guardar info en la tabla 
    comment = Comment.objects.create(name = "Alex")   # ---> de esta manera puedes guardar info en la tabla tambien
    return HttpResponse("Ruta para probar la creacion de modelos")

def delete(request):
    #comment = Comment.objects.get(id = 1)
    #comment.delete()

    Comment.objects.filter(id = 2).delete()
    return HttpResponse("Prueba de Borrado")