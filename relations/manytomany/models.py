from django.db import models

class Publication(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline=models.CharField(max_length=100)
    publications=models.ManyToManyField(Publication)     # en estas no lleva el on_delete

    def __str__(self):
        return self.headline
