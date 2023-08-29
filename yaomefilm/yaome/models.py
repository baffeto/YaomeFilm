from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    title = models.CharField('Название', max_length=1024)
    description = models.TextField()
    year_of_release = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    category = models.ManyToManyField('Category', related_name='actor')
    actors = models.ManyToManyField('Actor', related_name='actor')
    country = models.ForeignKey('Country', related_name='country', on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey('Director', related_name='director', on_delete=models.SET_NULL, null=True)
    
class Actor(models.Model):
    name = models.CharField('Имя', max_length=1024)
    surname = models.CharField('Фамилия', max_length=1024)
    
    def __str__(self) -> str:
        return f'{self.name} {self.surname}'
    
class Category(models.Model):
    name = models.CharField('Категория', max_length=32)
    
class Director(models.Model):
    name = models.CharField('Имя', max_length=1024)
    surname = models.CharField('Фамилия', max_length=1024)
    
class Country(models.Model):
    name = models.CharField("Название страны", max_length=56, unique=True)
    
class Reviews(models.Model):
    content = models.TextField()
    film = models.ForeignKey(Film, related_name='film', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    