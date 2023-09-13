# DNC Challenge

Este é um projeto em Python e Django com a solução do [desafio de Software Engineer PL](https://dncgroupbr.notion.site/Software-Eng-PL-081ea335ef5c454f96074726601563f4).

![Diagrama de solução](https://i.imgur.com/Jf9jObp.png)

## Requisitos

O sistema deve ser capaz de:

- Armazenar os dados dos alunos, das escolas e das notas.
- Exibir as pontuações dos alunos em diferentes escolas e categorias, e atualizá-las em tempo real.
- Permitir que os usuários insiram notas para os alunos, e calcular a pontuação de cada aluno com base nas notas.
- Garantir a consistência, a segurança e a escalabilidade do sistema.

## Componentes principais

O sistema pode ser dividido em três componentes principais:

- Front-end: É a parte do sistema que interage com os usuários, através de uma interface web. Ele é responsável por exibir as informações do sistema, como as escolas, os alunos, as notas e o ranking. Ele também é responsável por enviar os dados do formulário de inserção de nota para o back-end. Como o foco do desafio é voltado para programação Back-end, aqui só utilizarei HTML.
- Back-end: É a parte do sistema que processa as requisições do front-end, através de uma API REST. Ele é responsável por gerenciar os dados do sistema, como os alunos, as escolas e as notas. Ele também é responsável por calcular a pontuação dos alunos com base nas notas, e atualizar o ranking em tempo real. Ele será desenvolvido usando Python e Django.
- Banco de dados: É a parte do sistema que armazena os dados do sistema, como os alunos, as escolas e as notas. Ele é responsável por garantir a persistência, a integridade e a consistência dos dados. Aqui será utilizado o PostgreSQL.

## Tecnologias usadas

- Python
- Django
- HTML
- PostgreSQL
- Docker

## Interface

A interface entre os diferentes componentes do sistema pode ser definida da seguinte forma:

- Front-end -> Back-end: O front-end se comunica com o back-end através de uma API REST, usando o protocolo HTTP e o formato JSON. Temos as seguintes endpoints:
    - GET `/` : Retorna uma lista de todas as escolas e os 3 primeiros colocados gerais.
    - GET `/escola/<id>/` : Retorna os detalhes de uma escola específica e os 10 primeiros colocados da escola.
    - GET `/aluno/<id>/` : Retorna os detalhes de um aluno específico e as suas notas.
    - GET `/nota/` : Disponibiliza um formulário de inserção de nota e envia a requisição via POST para si mesmo.
    - POST `/nota/` : Recebe os dados do formulário de inserção de nota e cria um objeto do modelo Nota com esses dados.
    - GET `/admin/` : Utilizada para criação de escolas e alunos.
- Back-end -> Banco de dados: O back-end se comunica com o banco de dados através de um ORM (Object-Relational Mapper), que abstrai as operações SQL e permite manipular os dados como objetos Python. O ORM usado pelo Django é o Django ORM.

## Modelo de dados

![MER da base de dados](https://i.imgur.com/seItnrO.png)

## Como instalar e usar

Para instalar e usar este projeto, siga os seguintes passos:

### Via Docker

1. Execute o comando `git config --global core.autocrlf false`

2. Clone este repositório

3. Utilize o comando `docker-compose up` e aguarde o término do processo (termina quando iniciar o servidor web)

4. Vá para o passo 6

### Local

1. Clone este repositório

2. Instale as dependências do projeto:
- `pip3 install -r requirements.txt`

3. Faça as migrações do banco de dados:
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

4. Popule o banco de dados:
- `python3 populate_db.py`

5. Rode o servidor de desenvolvimento:
- `python3 manage.py runserver`

6. Acesse o app no navegador ou em algum cliente HTTP:

- `http://localhost:8000/` ou `http://127.0.0.1:8000/` para ver o pódium
- rota `/admin` para criar escolas e alunos -> user = luiz, senha = luiz
- rota `/nota` para adicionar ou atualizar notas de alunos

7. Os testes unitários podem ser visualizados no arquivo `ranking/tests.py`

- O Django facilita a criação dos testes dos modelos e das views por meio de classes.
    - Em ambos primeiro criamos alguns objetos de teste, e primeiro na classe `ModelTestCase` verificamos se eles foram criados corretamente.
    - Passando essa primeira bateria, vamos para os testes das nossas endpoints na classe `ViewTestCase`. Aqui verificamos se todas as nossas rotas estão recebendo e repassando os dados conforme definimos no nosso design de solução.
