from pydatics import BaseModel

class Produto(BaseModel):
    id: int = None
    nome: str
    preco: float
    quantidade: int