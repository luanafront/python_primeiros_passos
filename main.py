from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

banco = []


##len() é usado para pegar o tamnho. No javascript é length

class Nota(BaseModel):
    nome: str
    nota: float  # numero com ponto


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, churros: Union[str, None] = None):
    return {"item_id": item_id, "churros": churros}


@app.get("/verificarSeEPar/{num}")
def verificar_par(num: int):
    if num % 2 == 0:
        return True
    return False


@app.post("/notas/cadastrar/")
def cadastrar_nota(nota: Nota):
    banco.append(nota.nota)
    return {
        "notas": banco
    }


@app.get("/notas/media/")
def media_notas():
    resultado = calcular_media_banco()
    return {
        "media": resultado
    }


def calcular_media_banco():
    soma = total_de_notas()

    resultado = 0
    tamanho_do_banco = len(banco)

    if tamanho_do_banco != 0:
        resultado = soma / tamanho_do_banco
    return resultado


def total_de_notas():
    soma = 0
    for nota in banco:
        soma += nota
    return soma


@app.get("/notas/status/")
def status_notas():
    media = calcular_media_banco()
    if media < 6:
        return "A turma está de recuperação"
    return "A turma passou"
