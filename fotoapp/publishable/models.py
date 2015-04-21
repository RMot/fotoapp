from django.db import models


# Create your models here.
class Publishable(models.Model):
    publish_date = models.DateTimeField('fecha de publicacion', null=True)

    class Meta:
        abstract = True