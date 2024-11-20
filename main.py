from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from service import FibonacciService

app = FastAPI()

class TimeInput(BaseModel):
    time: str  # Formato HH:MM:SS

def fibonacci_series(x, y, n):
    series = [x, y]
    for _ in range(n):
        series.append(series[-1] + series[-2])
    return series
@app.get("/")
def read_root():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    return FibonacciService().get_fibonacci_from_time(time_str)

@app.post("/fibonacci")
def get_fibonacci_series(time_input: TimeInput):
    return FibonacciService().get_fibonacci_from_time(time_input.time)