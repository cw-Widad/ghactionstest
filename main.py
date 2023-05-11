from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from math import sqrt, factorial

class AdditionPayloadBody(BaseModel):
    numbers: list
class Payloadtwo(BaseModel):
    number1: Union[int,float]
    number2: Union[int,float]

class Payloadone(BaseModel):
    number: Union[int,float]

app = FastAPI()

@app.get("/")
async def root():
    return {"Use /docs for interactive use"}

@app.post("/addition")
def addition(payload: AdditionPayloadBody):
    sumadd = sum(payload.numbers)
    return f"sum of numbers {[i for i in payload.numbers]}: {sumadd}"
    
@app.post("/squareroot")
def squareroot(payload: Payloadone ):
    squareroot = sqrt(payload.number)
    return f"square root of {payload.number} is : {squareroot}"

@app.post("/factorial")
def squareroot(payload: Payloadone ):
    factorialnum = factorial(payload.number)
    return f"factorial root of {payload.number} is : {factorialnum}"

@app.post("/difference")
def difference(payload: Payloadtwo):
    diff = payload.number1 - payload.number2
    return {"number1": payload.number1, "number2": payload.number2, "difference": diff}

@app.post("/product")
def product(payload: Payloadtwo):
    product = payload.number1 * payload.number2
    return {"number1": payload.number1, "number2": payload.number2, "product": product}

@app.post("/division")
def product(payload: Payloadtwo):
    quotient = payload.number1 / payload.number2
    return {"number1": payload.number1, "number2": payload.number2, "quotient": quotient}

