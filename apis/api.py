from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Ejemplo de modelo con campos para el endpoint
class Datos(BaseModel):
    nombre: str
    edad: int

# Endpoint GET que muestra el mensaje 'Hello World'
@app.get("/obtener-datos", 
        description="""
        Los endpoint GET sirven para obtener datos.
        \nPulsa en 'Try it out' y 'Execute' para obtener el mensaje 'Hello World'
        """)
def obtiene_datos():
    return {"message": "Hello World"}

@app.post("/introducir-datos", 
        description="""
        Los endpoint POST sirven para crear datos.
        \nPulsa en 'Try it out' e introduce en el payload un nombre y una edad
        \ny pulsa 'Execute' para ver el resultado
        """)
def introduce_datos(data: Datos):
    nombre=data.nombre
    edad=data.edad
    
    return {f"El nombre es '{nombre}' y la edad es '{edad}'"}

@app.delete("/eliminar-datos", 
        description="""
        Los endpoint DELETE eliminan datos.
        \nPulsa en 'Try it out' y 'Execute' para obtener el mensaje 'Datos eliminados'
        """)
def eliminar_datos():
    return {"Datos ficticios eliminados"}

@app.put("/actualizar-datos", 
        description="""
        Los endpoint PUT actualizan datos.
        \nPulsa en 'Try it out' e introduce en el payload un nombre y una edad
        \ny pulsa 'Execute' para ver el resultado
        """)
def actualizar_datos(data: Datos):
    nombre=data.nombre
    edad=data.edad
    
    return {f"Nombre y edad actualizados a '{nombre}'' y '{edad}'"}