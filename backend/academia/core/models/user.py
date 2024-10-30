from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (('personal', 'Personal Trainer'), ('aluno', 'Aluno'))
    role = models.CharField(max_length=10, choices=ROLES)
    password = models.CharField(max_length=128)
    # Dados específicos para o aluno
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)  # Peso
    height = models.FloatField(null=True, blank=True)  # Altura
    fat_percentage = models.FloatField(null=True, blank=True)  # Percentual de gordura
    muscle_mass = models.FloatField(null=True, blank=True)  # Massa muscular
    health_history = models.TextField(null=True, blank=True)  # Histórico de saúde
