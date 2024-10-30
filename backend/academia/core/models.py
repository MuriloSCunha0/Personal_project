# core/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    ROLE_CHOICES = (
        ('personal', 'Personal Trainer'),
        ('aluno', 'Aluno')
    )
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    fat_percentage = models.FloatField(null=True, blank=True)
    muscle_mass = models.FloatField(null=True, blank=True)
    health_history = models.TextField(null=True, blank=True)

class WorkoutPlan(models.Model):
    DAYS_OF_WEEK = (
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    )
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    personal = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_workouts')
    day_of_week = models.CharField(max_length=15, choices=DAYS_OF_WEEK)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Exercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    description = models.TextField()
    sets = models.PositiveIntegerField()
    repetitions = models.CharField(max_length=50)
    rest_time = models.PositiveIntegerField()  # em segundos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Progress(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='progress')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    repetitions = models.PositiveIntegerField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)