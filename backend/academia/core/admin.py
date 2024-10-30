from django.contrib import admin
from .models import User, WorkoutPlan, Exercise, Progress

admin.site.register(User)
admin.site.register(WorkoutPlan)
admin.site.register(Exercise)
admin.site.register(Progress)
