from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 

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
def salvar_produtos():
    return "Produto salvo com sucesso!"
# python -m uvicorn main:app --reload -> ligando o servidor pelo terminal