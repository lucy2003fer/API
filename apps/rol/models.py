# app_roles/models.py
from django.db import models

class Rol(models.Model):
    ROLES = [
        ('tecnico', 'Técnico'),
        ('catador', 'Catador'),
        ('barista', 'Barista'),
    ]
    rol=models.CharField(max_length=20, choices=ROLES)
    
    def __str__(self):
        return self.rol
