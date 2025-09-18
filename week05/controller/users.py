# week05/controller/users.py

from fastapi import APIRouter
from typing import Union

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}