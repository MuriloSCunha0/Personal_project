from django.contrib.auth.models import AbstractUser
from django.db import models
from services.google_drive_service import get_video_url_from_drive

class User(AbstractUser):
    ROLE_CHOICES = (('personal', 'Personal Trainer'), ('aluno', 'Aluno'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    fat_percentage = models.FloatField(null=True, blank=True)
    muscle_mass = models.FloatField(null=True, blank=True)
    health_history = models.TextField(null=True, blank=True)

class WorkoutPlan(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    day_of_week = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

class Exercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)  # Nome do exercício
    sets = models.PositiveIntegerField()  # Séries
    repetitions = models.PositiveIntegerField()  # Repetições
    weight = models.FloatField()  # Peso utilizado
    rest_time = models.DurationField()  # Tempo de descanso
    video_url = models.URLField(max_length=255, blank=True)  # Link para o vídeo no Google Drive

    def save(self, *args, **kwargs):
        # Atualizar o campo 'video_url' com base no nome do exercício
        self.video_url = get_video_url_from_drive(self.name)
        super().save(*args, **kwargs)

class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed_sets = models.PositiveIntegerField()
    completed_repetitions = models.PositiveIntegerField()
    used_weight = models.FloatField()
    rest_time = models.DurationField()
    date = models.DateTimeField(auto_now_add=True)
