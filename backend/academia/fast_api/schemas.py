from pydantic import BaseModel
from typing import List, Optional

class ExerciseBase(BaseModel):
    name: str
    sets: int
    repetitions: int
    weight: float
    rest_time: str
    video: Optional[str] = None

class ExerciseCreate(ExerciseBase):
    pass

class Exercise(ExerciseBase):
    id: int
    workout_plan_id: int

    class Config:
        orm_mode = True

class WorkoutPlanBase(BaseModel):
    day_of_week: str

class WorkoutPlanCreate(WorkoutPlanBase):
    student_id: int

class WorkoutPlan(WorkoutPlanBase):
    id: int
    student_id: int
    created_at: str
    exercises: List[Exercise] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    fat_percentage: Optional[float] = None
    muscle_mass: Optional[float] = None

    class Config:
        orm_mode = True