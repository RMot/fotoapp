from django.db import models
from publishable.models import Publishable
from authorable.models import Authorable
from timestampable.models import Timestampable
from fotos.models import Photo

# Create your models here.
class Event(Publishable, Authorable, Timestampable, models.Model):
    name = models.CharField('descripcion', max_length=50)
    photos = models.ManyToManyField(Photo)
