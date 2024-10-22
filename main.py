from fastapi import FastAPI
import loguru
import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
app1 = FastAPI()
from pydantic import BaseModel
class validated_user(BaseModel):
    name:str
    surname:str
    age:int
    registration_date:datetime.date
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
@app1.post("/user/validate", summary = "регистрация(валидация) юзера")
def validate(user:validated_user):
    return user.name +" "+ user.surname +" " + str(user.age)+" Years old, registration_date: "+datetime.datetime.strftime(user.registration_date, "%d.%m.%Y:")
@app1.get("/user/information", summary = "Вывод информации о пользователе")
def get_information(user_id:int):
    connection = psycopg2.connect(database = "ba", host = "localhost", user = "postgres", password = "XomiakiNePlachut1", cursor_factory = RealDictCursor)
    cursor = connection.cursor()
    cursor.execute(f"""
    select * from public.mydata
    where client_id = {user_id}
    """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


