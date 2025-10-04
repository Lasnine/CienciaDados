from pydantic import BaseModel

class Cadastro(BaseModel):
    id: int = None
    nome: str
    email: str
    telefone: str