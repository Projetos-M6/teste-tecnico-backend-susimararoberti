<h1 align="center">CNAB</h1>

## 💻 Projeto

API destinada a parsear arquivos txt para formato json, salvando em banco de dados e retornando seus dados.

## 🔨 Tecnologias utilizadas

- Django
- Django Rest Framework

## ✨ Instalação

### 1 - Clone o repositório na sua máquina

### 2 - Crie suas variáveis de ambiente

- Esse projeto está utilizando PostgreSQL;
- Crie um arquivo `.env` na raiz do projeto -> siga o padrão de `.env.example`;

### 3 - Crie seu ambiente virtual

- Comece pelo comando `python -m venv venv`
- Linux: rode em seguida o comando `source venv/bin/activate`
- Windows: rode em seguida o comando `.\venv\Scripts\activate`

### 4 - Instale as dependências da aplicação

- Para isso basta utilizar o comando `pip install -r requirements.txt`

### 5 - Rode as migrações da aplicação

- É importante que você rode as migrações;
- Utilize o comando `python manage.py migrate`

### 6 - Inicialize a aplicação

- Basta rodar o comando `python manage.py runserver`
- Para encerrar, rode `Ctrl+c`

### 7 - Vizualizando a aplicação localmente

- Para visualizar as rotas acesse a documentação em [http://localhost:8000/api/swagger-doc/](http://localhost:8000/api/swagger-doc/)

### 8 - Testando/Utilizando a aplicação localmente

#### Método POST:

- Utilize a rota `http://localhost:8000/api/parser/cnab`
- Envie um `Binary File` no formato txt

#### Método GET:

- Utilize a rota `http://localhost:8000/api/relatorio/<NOME DA LOJA>/`

### 9 - Usando o deploy

- Utilize o endpoint `https://cnab-susimara.herokuapp.com/api/parser/cnab` para realizar o upload do arquivo txt CNAB;
- Utilize o endpoint `https://cnab-susimara.herokuapp.com/api/relatorio/<NOME DA LOJA>/` para realizar a consulta das operações e saldo de uma loja específica;
- Utilize o endpoint [https://cnab-susimara.herokuapp.com/api/swagger-doc/](https://cnab-susimara.herokuapp.com/api/swagger-doc/) para consultar a documentação da aplaicação;
