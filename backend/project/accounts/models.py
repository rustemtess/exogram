from django.db import models
from django.contrib.auth.models import User

class User(models.User):
    models.EmailField( max_length=254)
    username = models.CharField(max_length=30)
    password = models.CharField(min_length=8, max_length=32)