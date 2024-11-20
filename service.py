from datetime import datetime


class FibonacciService:
    def __init__(self):
        pass

    def fibonacci_series(self, x, y, n):
        series = [x, y]
        for _ in range(n):
            series.append(series[-1] + series[-2])
        return series

    def get_fibonacci_from_time(self, time_str):
        try:
            time = datetime.strptime(time_str, "%H:%M:%S")
        except ValueError:
            return {"error": "Formato de hora inválido. Use HH:MM:SS"}

        x = time.minute % 10  # Semilla X (último dígito de los minutos)
        y = time.minute // 10  # Semilla Y (primer dígito de los minutos)
        n = time.second  # Cantidad de números a mostrar

        series = self.fibonacci_series(x, y, n)
        return {"series": series[::-1]}  # Devolver la serie en orden descendente