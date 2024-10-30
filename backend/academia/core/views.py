# core/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import WorkoutPlan, Exercise, Progress, User
from .serializers import (
    WorkoutPlanSerializer, ExerciseSerializer,
    ProgressSerializer, UserSerializer
)

class IsPersonalTrainerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'personal'

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated, IsPersonalTrainerOrReadOnly]

    def get_queryset(self):
        if self.request.user.role == 'personal':
            return WorkoutPlan.objects.filter(personal=self.request.user)
        return WorkoutPlan.objects.filter(student=self.request.user)

    @action(detail=True, methods=['post'])
    def assign_exercises(self, request, pk=None):
        workout_plan = self.get_object()
        exercises_data = request.data.get('exercises', [])
        
        created_exercises = []
        for exercise_data in exercises_data:
            exercise = Exercise.objects.create(
                workout_plan=workout_plan,
                **exercise_data
            )
            created_exercises.append(exercise)
        
        serializer = ExerciseSerializer(created_exercises, many=True)
        return Response(serializer.data)

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated, IsPersonalTrainerOrReadOnly]

    def get_queryset(self):
        if self.request.user.role == 'personal':
            return Exercise.objects.filter(workout_plan__personal=self.request.user)
        return Exercise.objects.filter(workout_plan__student=self.request.user)

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'personal':
            return Progress.objects.filter(exercise__workout_plan__personal=self.request.user)
        return Progress.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
