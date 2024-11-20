from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

from core import database
from service import FibonacciService

app = FastAPI()


database.Base.metadata.create_all(bind=database.engine)


class TimeInput(BaseModel):
    time: str  # Formato HH:MM:SS


@app.get("/")
async def read_root():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    return await FibonacciService().get_fibonacci_from_time(time_str)

@app.post("/fibonacci")
async def get_fibonacci_series(time_input: TimeInput):
    return await FibonacciService().get_fibonacci_from_time(time_input.time)
