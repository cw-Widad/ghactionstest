from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class AdditionPayloadBody(BaseModel):
    summantOne: int
    summantTwo: int

class DifferencePayloadBody(BaseModel):
    subtrahentOne: int
    subtrahentTwo: int

class ProductPayloadBody(BaseModel):
    factorOne: int
    factorTwo: int

class DivisionPayloadBody(BaseModel):
    divisorOne: int
    divisorTwo: int

app = FastAPI()

@app.post("/addition")
def addition(payload: AdditionPayloadBody):
    sum = payload.summantOne + payload.summantTwo
    return {"number1": payload.summantOne, "number2": payload.summantTwo, "sum": sum}

@app.post("/difference")
def difference(payload: DifferencePayloadBody):
    diff = payload.subtrahentOne - payload.subtrahentTwo
    return {"subtrahentOne": payload.subtrahentOne, "subtrahentTwo": payload.subtrahentTwo, "difference": diff}

@app.post("/product")
def product(payload: ProductPayloadBody):
    product = payload.factorOne * payload.factorTwo
    return {"factorOne": payload.factorOne, "factorTwo": payload.factorTwo, "product": product}

@app.post("/division")
def product(payload: DivisionPayloadBody):
    quotient = payload.divisorOne / payload.divisorTwo
    return {"divisorOne": payload.divisorOne, "divisorTwo": payload.divisorTwo, "quotient": quotient}

