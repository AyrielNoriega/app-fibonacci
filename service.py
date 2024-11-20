from datetime import datetime

from models import FibonacciSeries
from schemas import FibonacciSeries as FibonacciSeriesSchema , FibonacciSeriesCreate
from core.database import Session

class FibonacciService:
    def __init__(self):
        self.db = Session()


    async def fibonacci_series(self, x, y, n):
        series = [x, y]
        for _ in range(n):
            series.append(series[-1] + series[-2])
        return series


    async def get_fibonacci_from_time(self, time_str):
        try:
            time = datetime.strptime(time_str, "%H:%M:%S")
        except ValueError:
            return {"error": "Formato de hora inválido. Use HH:MM:SS"}

        x = time.minute % 10  # Semilla X (último dígito de los minutos)
        y = time.minute // 10  # Semilla Y (primer dígito de los minutos)
        n = time.second  # Cantidad de números a mostrar

        series = await self.fibonacci_series(x, y, n)

        series_str = ",".join(map(str, series[::-1]))  # a una cadena

        db_series = FibonacciSeriesCreate(time_str=time_str, series=series_str)
        self.save_series(db_series)

        return {"series": series[::-1]}  # Devolver la serie en orden descendente


    def save_series(self, series: FibonacciSeriesCreate):
        db_series = FibonacciSeries(time_str=series.time_str, series=series.series)
        self.db.add(db_series)
        self.db.commit()
        self.db.refresh(db_series)
        return db_series