from rest_framework import viewsets
from models.train import WorkoutPlan, Exercise, Progress
from serializers.settings import WorkoutPlanSerializer, ExerciseSerializer, ProgressSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
