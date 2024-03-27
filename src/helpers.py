# src/helpers.py

from db import SessionLocal
from models.task import Task

def exit_program():
    print("Exiting the program...")
    # Any cleanup code can go here
    exit()

def create_task():
    session = SessionLocal()
    try:
        task_name = input("Enter task name: ")
        task = Task(name=task_name)
        session.add(task)
        session.commit()
        print("Task created successfully!")
    except Exception as e:
        print("Error creating task:", e)
    finally:
        session.close()

def delete_task():
    session = SessionLocal()
    try:
        task_id = int(input("Enter task ID to delete: "))
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)
            session.commit()
            print("Task deleted successfully!")
        else:
            print("Task not found!")
    except Exception as e:
        print("Error deleting task:", e)
    finally:
        session.close()

def show_all_tasks():
    session = SessionLocal()
    try:
        tasks = session.query(Task).all()
        print("All tasks:")
        for task in tasks:
            print(f"ID: {task.id}, Name: {task.name}")
    except Exception as e:
        print("Error fetching tasks:", e)
    finally:
        session.close()

def show_task():
    session = SessionLocal()
    try:
        task_id = int(input("Enter task ID to show: "))
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            print(f"ID: {task.id}, Name: {task.name}")
        else:
            print("Task not found!")
    except Exception as e:
        print("Error fetching task:", e)
    finally:
        session.close()
