from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from fotos.models import Photo


class PhotoList(ListView):
    model = Photo
    context_object_name = 'disponible_photos'