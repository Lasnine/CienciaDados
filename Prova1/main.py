from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from cadastro import Cadastro
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="prova1"
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

@app.post("/cadastro")
def salvar_cadastro(cadastro: Cadastro):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        print("Conectado ao banco.")
        print("Dados recebidos:", cadastro)

        sql = "INSERT INTO cadastro (nome, email, telefone) VALUES (%s, %s, %s)"
        valores = (cadastro.nome, cadastro.email, cadastro.telefone)
        cursor.execute(sql, valores)

        conn.commit()
        print("Cadastro inserido com sucesso.")

        return {"message": "Cadastro salvo com sucesso!"}
    
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ou inserir no banco: {err}")
        return {"error": "Erro ao salvar cadastro no banco de dados"}
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# python -m uvicorn main:app --reload -> ligando o servidor pelo terminal