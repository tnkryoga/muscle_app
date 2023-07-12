from typing import List
from fastapi import APIRouter
import api.schemas.user as user_schema

router = APIRouter()


@router.get("/tasks", response_model=List[user_schema.User])
async def list_users():
    return [user_schema.User(id=1, title="1つ目のTODOタスク")]


@router.post("/users")
async def create_task():
    pass


@router.put("/users/{task_id}")
async def update_task():
    pass


@router.delete("/users/{task_id}")
async def delete_task():
    pass