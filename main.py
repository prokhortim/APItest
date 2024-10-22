from fastapi import FastAPI

import datetime
app1 = FastAPI()

@app1.get("/")
def function():
    return "Hello, world"
@app1.get("/sum_numbers", summary = "Вывод суммы двух чисел")
def numbers_sum(a:int,b:int) -> int:
    """ что вы хотели здесь увидеть???"""
    return a+b
@app1.get("/sum_date", summary = "вычисляет дату по начальной дате и изменению в днях")
def date_diff(current_date:datetime.date, offset : int):
    x = (current_date + datetime.timedelta(days = offset))
    return x


