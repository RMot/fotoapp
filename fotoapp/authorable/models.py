from django.db import models
from django.contrib.auth.models import User

class Authorable(models.Model):
    user = models.ForeignKey(User)

    class Meta:
        abstract = True