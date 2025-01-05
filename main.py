from datetime import datetime
from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel

from core import database
from users.router.auth import auth_router
from fibonacci.router import fibonacci_router
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


app.include_router(fibonacci_router)
app.include_router(auth_router)


@app.get("/test_users")
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
