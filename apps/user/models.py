from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.rol.models import Rol 

class User(AbstractUser):
    rol=models.ForeignKey(Rol, on_delete=models.SET_NULL,null=True)