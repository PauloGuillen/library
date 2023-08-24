# library Api

Esta é uma aplicação de armazenamento de dados de livros e autores, para uma biblioteca. Para atender os requisitos, foi desenvolvida uma HTTP REST API no
backend.
Os registros dos autores, no banco de dados, contém os seguintes
campos:
- id (gerado automaticamente, não sequencial)
- name

Já os livros, contém os seguintes campos:
- id (gerado automaticamente, não sequencial)
- name
- edition
- publication_year
- authors (mais de um autor pode escrever um livro)

Um livro pode ser escrito por mais de um autor e um autor pode
escrever mais de um livro, portanto temos uma relação many-to-
many.

Estão implementadas as ações de listar os registros, como do
CRUD (Create, Read, Update and Delete), tanto para autores como
para os livros.

Listar e criar (GET), estão nos respectivos end point:
api/author
api/book
Exemplos:
https://pguillen-library.fly.dev/api/author/
https://pguillen-library.fly.dev/api/book/

Ler um registro, modificar e eliminar estão nos seguintes end
point, fornecendo a primary key:
api/author/<id>
api/book/<id>
Exemplos:
https://pguillen-library.fly.dev/api/author/13906209795772/
https://pguillen-library.fly.dev/api/book/178948800482864/

Os autores podem ser filtrados por name e os livros por name,
edition e publication_year. 
Exemplos:
https://pguillen-library.fly.dev/api/author/?name=ramalho
https://pguillen-library.fly.dev/api/book/?publication_year=2016

Para desenvolver a API, foram utilizadas as seguintes tecnologias:
Django Rest Framework, Postgres, Docker e Docker Compose.

A documentação da API está disponivel nos seguintes links:
https://pguillen-library.fly.dev/api/schema/swagger/
https://pguillen-library.fly.dev/api/schema/redoc/
https://pguillen-library.fly.dev/api/schema/

Caso queira executar a aplicação localmente, clone esse
repositório, tenha o docker compose instalado e na pasta library
do projeto e execute:
mv .env.example .env
docker compose build
docker compose up

Também, acesse os links:
http://localhost:8000/api/author/
http://localhost:8000/api/book/
http://localhost:8000/admin/
