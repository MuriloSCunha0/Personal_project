from django.db import models
from backend.academia.core.models.user import User

class WorkoutPlan(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    day_of_week = models.CharField(max_length=15)  # Segunda, Terça, etc.
    created_at = models.DateTimeField(auto_now_add=True)

class Exercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)  # Nome do exercício
    sets = models.PositiveIntegerField()  # Quantidade de séries
    repetitions = models.PositiveIntegerField()  # Quantidade de repetições
    weight = models.FloatField()  # Peso a ser utilizado
    rest_time = models.DurationField()  # Tempo de descanso entre séries
    video_url = models.URLField(max_length=255, blank=True)  # Vídeo explicativo

class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed_sets = models.PositiveIntegerField()  # Séries realizadas
    completed_repetitions = models.PositiveIntegerField()  # Repetições realizadas
    used_weight = models.FloatField()  # Peso utilizado
    rest_time = models.DurationField()  # Tempo de descanso real
    date = models.DateTimeField(auto_now_add=True)  # Data do registro
    