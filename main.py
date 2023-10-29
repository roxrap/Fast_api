from fastapi import FastAPI
from pydantic import BaseModel #para q los datos se correspondan con el tipo asignados en mi clase
app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int


#http://127.0.0.1:8000
#creo la ruta raiz para mi API a traves de decoradores
@app.get("/")
def index():
    return {"message" : "Hola. Probando mi nueva API de RR"}   #le entregamos un diccionario q fastapi va a convertir en un json

@app.get("/libros/{id}")
def mostrar_libro(id):
    return {"data": id}

@app.post("/libros")
def insertar_libro(libro:Libro):
    return {"message": f"libro {libro.titulo} insertado"}