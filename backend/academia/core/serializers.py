from rest_framework import serializers
from .models import User, WorkoutPlan, Exercise, Progress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'age', 'weight', 'height', 'fat_percentage', 'muscle_mass']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = serializers.StringRelatedField(many=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'student', 'day_of_week', 'exercises', 'created_at']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'sets', 'repetitions', 'weight', 'rest_time', 'video_url']

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
