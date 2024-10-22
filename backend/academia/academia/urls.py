from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import WorkoutPlanViewSet, ExerciseViewSet, ProgressViewSet

router = DefaultRouter()
router.register(r'workout-plans', WorkoutPlanViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'progress', ProgressViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
