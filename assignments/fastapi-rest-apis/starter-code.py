from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# TODO: Define the Task model here
class Task(BaseModel):
    pass


# TODO: Create an in-memory list to store tasks
tasks = []


# TODO: Implement GET route to retrieve all tasks
@app.get("/tasks")
async def get_tasks():
    pass


# TODO: Implement POST route to create a new task
@app.post("/tasks")
async def create_task(task: Task):
    pass


# TODO: Implement GET route to retrieve a single task by ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    pass


# TODO: Implement PUT route to update a task
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    pass


# TODO: Implement DELETE route to remove a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    pass
