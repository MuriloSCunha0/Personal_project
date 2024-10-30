from django.db import models
from backend.academia.core.models.user import User

class WorkoutPlan(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    day_of_week = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Exercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight = models.FloatField()
    rest_time = models.DurationField()
    video = models.FileField(upload_to='exercise_videos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed_sets = models.PositiveIntegerField()
    completed_repetitions = models.PositiveIntegerField()
    used_weight = models.FloatField()
    rest_time = models.DurationField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']