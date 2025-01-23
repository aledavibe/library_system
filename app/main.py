from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database, exceptions

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para cadastrar um livro
@app.post("/livros/", response_model=schemas.Livro)
def criar_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    return crud.criar_livro(db=db, livro=livro)

# Endpoint para listar livros
@app.get("/livros/", response_model=list[schemas.Livro])
def listar_livros(titulo: str = None, autor: str = None, db: Session = Depends(get_db)):
    return crud.listar_livros(db=db, titulo=titulo, autor=autor)

# Endpoint para atualizar quantidade de livros
@app.put("/livros/{livro_id}", response_model=schemas.Livro)
def atualizar_quantidade_livro(livro_id: int, quantidade: int, db: Session = Depends(get_db)):
    return crud.atualizar_quantidade_livro(db=db, livro_id=livro_id, quantidade=quantidade)

# Endpoint para registrar empréstimo
@app.post("/emprestimos/", response_model=schemas.Emprestimo)
def registrar_emprestimo(emprestimo: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    try:
        return crud.registrar_emprestimo(db=db, emprestimo=emprestimo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para registrar devolução de livro
@app.post("/devolucoes/{emprestimo_id}", response_model=schemas.Emprestimo)
def registrar_devolucao(emprestimo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.registrar_devolucao(db=db, emprestimo_id=emprestimo_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
