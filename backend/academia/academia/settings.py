from rest_framework import serializers
from backend.academia.core.models.user import User 
from backend.academia.core.models.train import WorkoutPlan, Exercise, Progress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = serializers.StringRelatedField(many=True)
    class Meta:
        model = WorkoutPlan
        fields = ['id', 'student', 'day_of_week', 'exercises']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
