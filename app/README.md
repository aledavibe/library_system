Sistema de Biblioteca

Descrição

O Sistema de Biblioteca é uma API desenvolvida com FastAPI que permite gerenciar empréstimos de livros em uma biblioteca. A API possui funcionalidades para cadastrar livros, realizar empréstimos e devoluções, e gerar multas em caso de atraso na devolução.

Funcionalidades
Livros

Cadastrar livro (título, autor, ano de publicação, quantidade disponível).
Listar livros com filtros por título ou autor.
Atualizar a quantidade disponível de livros.
Ver detalhes de um livro.
Empréstimos

Registrar o empréstimo de livros.
Registrar a devolução de livros.
Listar empréstimos ativos.
Regras de Negócio

Não é permitido emprestar livros se a quantidade disponível for 0.
O usuário pode emprestar no máximo 2 livros por vez.
O prazo para devolução é de 15 dias.
Caso haja atraso na devolução, será gerada uma multa de R$ 1,00 por dia de atraso.

Tecnologias Utilizadas

FastAPI: Framework web para construir APIs.
SQLAlchemy: ORM para interagir com o banco de dados SQLite.
SQLite: Banco de dados utilizado para armazenar as informações.
Pydantic: Biblioteca para validação de dados.

Pré-requisitos
Antes de rodar o projeto, verifique se você tem o Python 3.7+ instalado em seu computador.

Instale as dependências do projeto:

pip install -r requirements.txt

Como Rodar a API

Passo 1: Clonar o Repositório
Clone o repositório para a sua máquina local:

git clone https://github.com/aledavibe/library_system.git
cd library_system

Passo 2: Configurar o Ambiente Virtual (opcional, mas recomendado)

Se você quiser criar um ambiente virtual para isolar as dependências, execute os seguintes comandos:

No Windows:

python -m venv venv
.\venv\Scripts\activate

No Linux/MacOS:

python3 -m venv venv
source venv/bin/activate

Passo 3: Instalar as Dependências

Instale as dependências do projeto:

pip install -r requirements.txt

Passo 4: Rodar o Servidor

Agora, você pode rodar o servidor utilizando o Uvicorn:

uvicorn app.main:app --reload

A API estará disponível em http://127.0.0.1:8000.

Passo 5: Acessar a Documentação da API

O FastAPI gera automaticamente a documentação interativa da API. Para acessá-la, basta navegar até o seguinte endereço no seu navegador:

Swagger UI (para testar os endpoints interativamente):

http://127.0.0.1:8000/docs

OpenAPI (documentação em formato JSON):

http://127.0.0.1:8000/openapi.json

Estrutura de Diretórios
Aqui está a estrutura de diretórios do projeto:

library_system/
│
├── app/
│   ├── __init__.py
│   ├── main.py             # Arquivo principal com a instância FastAPI
│   ├── models.py           # Modelos do banco de dados (SQLAlchemy)
│   ├── schemas.py          # Definição dos esquemas de dados (Pydantic)
│   ├── crud.py             # Funções de manipulação de dados (CRUD)
│   ├── database.py         # Configuração do banco de dados
│   └── exceptions.py       # Exceções personalizadas
│
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo

Como Contribuir

Faça um fork deste repositório.
Crie uma nova branch (git checkout -b minha-feature).
Faça suas alterações e adicione testes, se necessário.
Commit suas alterações (git commit -m 'Adiciona nova funcionalidade').
Envie as alterações para o repositório remoto (git push origin minha-feature).
Abra um pull request explicando suas mudanças.