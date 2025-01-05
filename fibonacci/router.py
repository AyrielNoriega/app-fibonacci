from fastapi import APIRouter
from datetime import datetime
from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel

from core.config import get_settings
from fibonacci.service import FibonacciService
from users.schemas.user import User, UserRegister
from users.service import auth
settings = get_settings()

class TimeInput(BaseModel):
    time: str  # Formato HH:MM:SS


fibonacci_router = APIRouter()
fibonacci_router.tags = ["fibonacci"]

@fibonacci_router.get("/fibonacci", dependencies=[Depends(auth.get_current_active_user)])
async def get_current_fibonacci_series():
    print("get_current_fibonacci_series !!")
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    return await FibonacciService().get_fibonacci_from_time(time_str)

@fibonacci_router.post("/fibonacci")
async def create_fibonacci_series(
    time_input: TimeInput,
    current_user: Annotated[User, Depends(auth.get_current_active_user)]
):
    return await FibonacciService().get_fibonacci_from_time(time_input.time)


@fibonacci_router.get("/fibonacci/all", dependencies=[Depends(auth.get_current_active_user)])
async def get_all_fibonacci_series():
    service = FibonacciService()
    return service.get_all_series()