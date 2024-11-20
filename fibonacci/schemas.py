from pydantic import BaseModel

class FibonacciSeriesBase(BaseModel):
    time_str: str
    series: str

class FibonacciSeriesCreate(FibonacciSeriesBase):
    pass

class FibonacciSeries(FibonacciSeriesBase):
    id: int

    class Config:
        orm_mode = True