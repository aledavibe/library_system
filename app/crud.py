from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def criar_livro(db: Session, livro: schemas.LivroCreate):
    db_livro = models.Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

def listar_livros(db: Session, titulo: str = None, autor: str = None):
    query = db.query(models.Livro)
    if titulo:
        query = query.filter(models.Livro.titulo.contains(titulo))
    if autor:
        query = query.filter(models.Livro.autor.contains(autor))
    return query.all()

def atualizar_quantidade_livro(db: Session, livro_id: int, quantidade: int):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if db_livro:
        db_livro.quantidade_disponivel += quantidade
        db.commit()
        db.refresh(db_livro)
    return db_livro

def registrar_emprestimo(db: Session, emprestimo: schemas.EmprestimoCreate):
    db_livro = db.query(models.Livro).filter(models.Livro.id == emprestimo.livro_id).first()
    if db_livro and db_livro.quantidade_disponivel > 0:
        # Verificar se o usuário já possui 2 empréstimos
        usuario_emprestimos = db.query(models.Emprestimo).filter(models.Emprestimo.usuario_id == emprestimo.usuario_id, models.Emprestimo.data_devolucao == None).count()
        if usuario_emprestimos >= 2:
            raise ValueError("O usuário já possui 2 empréstimos ativos.")
        
        # Registrar o empréstimo
        db_emprestimo = models.Emprestimo(**emprestimo.dict(), data_emprestimo=date.today())
        db.add(db_emprestimo)
        db.commit()
        db.refresh(db_emprestimo)
        db_livro.quantidade_disponivel -= 1
        db.commit()
        db.refresh(db_livro)
        return db_emprestimo
    raise ValueError("Livro não disponível para empréstimo.")

def registrar_devolucao(db: Session, emprestimo_id: int):
    db_emprestimo = db.query(models.Emprestimo).filter(models.Emprestimo.id == emprestimo_id).first()
    if db_emprestimo and db_emprestimo.data_devolucao is None:
        atraso = (date.today() - db_emprestimo.data_emprestimo).days - 15
        if atraso > 0:
            db_emprestimo.multa = atraso
        db_emprestimo.data_devolucao = date.today()
        db.commit()
        db.refresh(db_emprestimo)
        db_livro = db.query(models.Livro).filter(models.Livro.id == db_emprestimo.livro_id).first()
        db_livro.quantidade_disponivel += 1
        db.commit()
        db.refresh(db_livro)
        return db_emprestimo
    raise ValueError("Empréstimo não encontrado ou já devolvido.")
