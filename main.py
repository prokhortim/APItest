from fastapi import FastAPI
app1 = FastAPI()
@app1.get("/")
def function():
    return "Hello, world"
@app1.get("/sum_numbers", summary = "Вывод суммы двух чисел")
def numbers_sum(a:int,b:int) -> int:
    """ что вы хотели здесь увидеть???"""
    return a+b

