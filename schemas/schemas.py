from pydantic import BaseModel
class AlunoSchema(BaseModel):
    nome: str
    email: str

class CursoSchema(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float = 0