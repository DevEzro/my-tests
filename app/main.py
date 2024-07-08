from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

@app.get("/Get-Prueba") #read
async def get_prueba():
    return {"message": "Get"}

@app.put("/Put-Prueba")
async def put_prueba():
    return {"message": "Put"}

@app.post("/Post-Prueba")
async def post_prueba():
    return {"message": "Post"}

@app.delete("/Delete-Prueba")
async def delte_prueba():
    return {"message": "Delete"}