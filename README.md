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



##############################################################################################################



Acessando o Swagger UI

O Swagger UI fornece uma interface interativa para explorar e testar os endpoints da API de forma visual. Após configurar o servidor FastAPI corretamente, você pode acessar o Swagger UI diretamente pelo navegador para interagir com a API.

Requisitos

Você deve ter a API rodando localmente ou em um servidor.
A API deve estar utilizando o FastAPI, que integra automaticamente o Swagger UI.
Passos para Acessar o Swagger UI

Rodar a API Localmente

Para começar, você precisa rodar a API em sua máquina local utilizando o Uvicorn. No terminal, dentro do diretório do seu projeto, execute o seguinte comando:

uvicorn app.main:app --reload

Isso iniciará o servidor localmente e permitirá que você acesse a API em http://127.0.0.1:8000.

Acessar o Swagger UI

Após iniciar o servidor, o Swagger UI estará disponível automaticamente. Para acessá-lo, basta abrir um navegador e digitar o seguinte endereço:

http://127.0.0.1:8000/docs


A página do Swagger UI será carregada e você verá a interface onde poderá interagir com os endpoints da sua API.

Interagir com os Endpoints

O Swagger UI exibirá todos os endpoints da API com base nas rotas definidas no seu código FastAPI.

Você pode clicar em cada endpoint para expandir as informações e ver detalhes como os parâmetros de entrada, tipos de resposta e descrições.

Para testar um endpoint, basta preencher os campos necessários (caso haja parâmetros) e clicar no botão "Execute".

O Swagger UI irá realizar a chamada HTTP para o servidor e exibirá a resposta diretamente na interface, incluindo status da resposta, cabeçalhos e o corpo da resposta (se houver).

Acessar a Documentação da OpenAPI

Se você preferir visualizar a documentação da API no formato OpenAPI JSON, pode acessá-la diretamente pelo seguinte endereço:

http://127.0.0.1:8000/openapi.json

Esse arquivo contém uma descrição detalhada dos endpoints e parâmetros da API em formato JSON e pode ser utilizado para gerar documentação adicional ou integrá-la com outras ferramentas.

Funcionalidades no Swagger UI

Explorar Endpoints: Todos os endpoints disponíveis na API estarão listados, com a opção de expandi-los para visualizar mais informações.

Testar a API: Você pode testar diretamente a API preenchendo os parâmetros requeridos e clicando em "Execute".

Ver Respostas: O Swagger UI exibirá as respostas da API, incluindo o status HTTP (200, 404, 500, etc.), os dados retornados e possíveis mensagens de erro.

Filtros de Pesquisa: Você pode utilizar filtros para buscar por rotas específicas na documentação.

Exemplos de Uso

Aqui estão alguns exemplos do que você pode fazer diretamente no Swagger UI:

Cadastrar um novo livro: Preencha os campos necessários (como título, autor, ano, etc.) e execute a chamada POST para criar um novo livro.

Listar livros: Você pode fazer uma requisição GET para listar todos os livros cadastrados, com a possibilidade de filtrar por título ou autor.

Registrar empréstimo: Faça uma requisição POST para registrar o empréstimo de livros, especificando os detalhes necessários, como o ID do livro e o usuário.

Registrar devolução: Para registrar a devolução de um livro, você pode enviar os dados necessários via POST e obter informações sobre o atraso e a multa, se aplicável.
