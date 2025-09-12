from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from produto import Produto
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aula1"
    )
app = FastAPI() 

app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
) 

@app.get("/") 
def rota_raiz(): 
    return {"message": "API está funcionando!"}

@app.post("/produtos")
def salvar_produtos(produto: Produto):
    print(produto.nome)
    print(produto.preco)
    print(produto.quantidade)

    return {"message": "Produto salvo com sucesso!"}
# python -m uvicorn main:app --reload -> ligando o servidor pelo terminal