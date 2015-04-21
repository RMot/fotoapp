# coding=utf-8
from django.db import models


class Photo(models.Model):
    name = models.CharField('name', max_length=80)
    image = models.ImageField('imágen')




# Create your models here.
