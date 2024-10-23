from fastapi import FastAPI
import loguru
import datetime
import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import HTTPException
from typing import List
from pydantic import BaseModel
app1 = FastAPI()
class validated_user(BaseModel):
    name:str
    surname:str
    age:int
    registration_date:datetime.date
class validated_user2(BaseModel):
    id:int
    ФИО:str
    Пол:str
    Возраст:int
    class Config:
        orm_mode = True
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
@app1.get("/user/information", summary = "Вывод информации о пользователе", response_model = validated_user2)
def get_information(user_id:int):
    conn_uri = "postgresql://postgres:XomiakiNePlachut1@localhost/ba"
    users = pd.read_sql("select client_id from public.mydata"
    ,conn_uri)
    if user_id not in list(users["client_id"]):
        raise HTTPException(404, detail = "user not found")
    else:
        result = pd.read_sql(f"select * from public.mydata where client_id = {user_id}", conn_uri)
        result = {"id" : int(list(result["client_id"])[0]), "ФИО":str(list(result["client"])[0]), "Пол":str(list(result["gender"])[0]), "Возраст":int(list(result["age"])[0])}
        return result

