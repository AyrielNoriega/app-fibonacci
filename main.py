from datetime import datetime
from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel

from core import database
from service import FibonacciService
from users.router.auth import auth_router
from core.config import get_settings
from users.schemas.user import User, UserRegister
from users.service.user import UserService
from users.service import auth
settings = get_settings()

app = FastAPI(
    openapi_prefix=settings.API_VERSION,
    title = settings.APP_NAME
)

database.Base.metadata.create_all(bind=database.engine)


class TimeInput(BaseModel):
    time: str  # Formato HH:MM:SS


@app.get("/fibonacci", tags=["fibonacci"], dependencies=[Depends(auth.get_current_active_user)])
async def get_current_fibonacci_series():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    return await FibonacciService().get_fibonacci_from_time(time_str)

@app.post("/fibonacci", tags=["fibonacci"])
async def create_fibonacci_series(
    time_input: TimeInput,
    current_user: Annotated[User, Depends(auth.get_current_active_user)]
):
    return await FibonacciService().get_fibonacci_from_time(time_input.time)


@app.get("/fibonacci/all", tags=["fibonacci"], dependencies=[Depends(auth.get_current_active_user)])
async def get_all_fibonacci_series():
    service = FibonacciService()
    return service.get_all_series()


app.include_router(auth_router)


@app.get("/test_user")
async def test_user():
    db = database.Session()

    # Crear un usuario de prueba
    user_service = UserService(db)
    test_user = UserRegister(
        name="jon",
        username="jon",
        email="jon@gmail.com",
        password="1234"
    )
    user_service.register(test_user)
    db.close()
