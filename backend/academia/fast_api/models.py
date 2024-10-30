from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "core_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String)
    password = Column(String)
    age = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    fat_percentage = Column(Float, nullable=True)
    muscle_mass = Column(Float, nullable=True)

class WorkoutPlan(Base):
    __tablename__ = "core_workoutplan"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("core_user.id"))
    day_of_week = Column(String)
    created_at = Column(String)

    exercises = relationship("Exercise", back_populates="workout_plan")

class Exercise(Base):
    __tablename__ = "core_exercise"

    id = Column(Integer, primary_key=True, index=True)
    workout_plan_id = Column(Integer, ForeignKey("core_workoutplan.id"))
    name = Column(String)
    sets = Column(Integer)
    repetitions = Column(Integer)
    weight = Column(Float)
    rest_time = Column(String)
    video = Column(String, nullable=True)

    workout_plan = relationship("WorkoutPlan", back_populates="exercises")