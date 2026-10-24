from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Publication

def create(request):
    art1 = Article(headline="Articulo Primero")
    art2 = Article(headline="Articulo Segundo")
    art3 = Article(headline="Articulo Tercero")
    art1.save()
    art2.save()
    art3.save()

    pub1=Publication(title="Publicacion Primera")
    pub2=Publication(title="Publicacion Segunda")
    pub3=Publication(title="Publicacion Tercera")
    pub4=Publication(title="Publicacion Cuarta")
    pub5=Publication(title="Publicacion Quinta")
    pub6=Publication(title="Publicacion Sexta")
    pub7=Publication(title="Publicacion Septima")
    pub1.save()
    pub2.save()
    pub3.save()
    pub4.save()
    pub5.save()
    pub6.save()
    pub7.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)

    art2.publications.add(pub4)
    art2.publications.add(pub5)

    art3.publications.add(pub6)
    art3.publications.add(pub7)

    #resultado=art1.publications.all()
    resultado=pub1.article_set.all()
    #art1.publications.remove(pub1)    ----> esto elimina la relacion entre este articulo y esa publicacion 

    return HttpResponse(resultado)
