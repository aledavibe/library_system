from fastapi import HTTPException

class LivroNaoDisponivelException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class UsuarioComEmprestimoExcedidoException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class EmpréstimoNaoEncontradoException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)
