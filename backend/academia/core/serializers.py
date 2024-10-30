# core/serializers.py
from rest_framework import serializers
from .models import User, WorkoutPlan, Exercise, Progress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'age', 'weight',
                 'height', 'fat_percentage', 'muscle_mass', 'health_history']
        read_only_fields = ['id', 'username', 'email']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ['id', 'student', 'personal', 'day_of_week', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'workout_plan', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'exercise', 'student', 'weight', 'repetitions', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']