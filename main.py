from datetime import datetime
from fastapi import FastAPI

app = FastAPI()



def fibonacci_series(x, y, n):
    series = [x, y]
    for _ in range(n):
        series.append(series[-1] + series[-2])
    return series

@app.get("/")
def read_root():
    now = datetime.now()
    x = now.minute % 10  # Semilla X (último dígito de los minutos)
    y = now.minute // 10  # Semilla Y (primer dígito de los minutos)
    n = now.second  # Cantidad de números a mostrar
    print(f"Hora: {now}")
    print(f"Semilla X: {x}, Semilla Y: {y}, N: {n}")
    series = fibonacci_series(x, y, n)
    return {"series": series[::-1]}  # serie en orden descendente