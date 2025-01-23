from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

# Modelo de Livro
class Livro(Base):
    __tablename__ = "livros"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String)
    ano = Column(Integer)
    quantidade_disponivel = Column(Integer)

    emprestimos = relationship("Emprestimo", back_populates="livro")

# Modelo de Empréstimo
class Emprestimo(Base):
    __tablename__ = "emprestimos"
    
    id = Column(Integer, primary_key=True, index=True)
    livro_id = Column(Integer, ForeignKey("livros.id"))
    usuario_id = Column(Integer)
    data_emprestimo = Column(Date)
    data_devolucao = Column(Date, nullable=True)
    multa = Column(Integer, default=0)
    
    livro = relationship("Livro", back_populates="emprestimos")
