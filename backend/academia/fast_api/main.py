from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from typing import List

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@app.post("/workout-plans/", response_model=schemas.WorkoutPlan)
def create_workout_plan(workout_plan: schemas.WorkoutPlanCreate, db: Session = Depends(get_db)):
    db_workout_plan = models.WorkoutPlan(**workout_plan.dict())
    db.add(db_workout_plan)
    db.commit()
    db.refresh(db_workout_plan)
    return db_workout_plan

@app.get("/workout-plans/", response_model=List[schemas.WorkoutPlan])
def read_workout_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workout_plans = db.query(models.WorkoutPlan).offset(skip).limit(limit).all()
    return workout_plans

@app.post("/exercises/", response_model=schemas.Exercise)
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    db_exercise = models.Exercise(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

@app.get("/exercises/", response_model=List[schemas.Exercise])
def read_exercises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    exercises = db.query(models.Exercise).offset(skip).limit(limit).all()
    return exercises