from pydantic import BaseModel
from datetime import date
from typing import Optional

# Esquema para o Livro
class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano: int
    quantidade_disponivel: int

class LivroCreate(LivroBase):
    pass

class Livro(LivroBase):
    id: int
    
    class Config:
        orm_mode = True

# Esquema para Empréstimo
class EmprestimoBase(BaseModel):
    usuario_id: int
    livro_id: int

class EmprestimoCreate(EmprestimoBase):
    pass

class Emprestimo(EmprestimoBase):
    id: int
    data_emprestimo: date
    data_devolucao: Optional[date] = None
    multa: int = 0

    class Config:
        orm_mode = True
