# Desafio-Magalu
O Magalu está expandindo seus negócios e uma das novas missões do time de
tecnologia é criar uma funcionalidade de Produtos Favoritos de nossos Clientes, em
que os nossos aplicativos irão enviar requisições HTTP para um novo backend que
deverá gerenciar nossos clientes e seus produtos favoritos.
Esta nova API REST será crucial para ações de marketing da empresa e terá um
grande volume de requisições então tenha em mente que a preocupação com
performance é algo que temos em mente constantemente..


## Instalação
Aplicação requer Python3.8, Django3 e Django Rest Framework e Git para executar.
```sh
$ git clone https://github.com/rodrigobu/magalu.git
```
Crie uma nova virtualenv:
```sh
$ virtualenv myenv -p python3
```

Depois de criar a virtualenv ative:
```sh
$ source myenv/bin/activate
```
Vamos para repositorio:
```sh
(myenv) ~$ cd magalu/
```
Instalaremos as bibliotecas nescessária que estão no arquivo requirements.txt
```sh
(myenv) ~$ pip install -r requirements.txt
```
Criaremos o Banco de dados para fazer o migrate.
```sh
(myenv) ~$ psql
```
```sh
(myenv) postgres=# CREATE DATABASE magalu;
```
Após as instalações das bibliotecas precisamos fazer o migrate para que funcione as alterações de banco.
```sh
python manage.py migrate
```
Agora já temos nosso ambiente instalado, já conseguimos acessar nossa aplicação.

## Como Usar
Podemos executar o projeto de duas formas, via navegador ou API, para qualquer um dos metodos precisamo deixar o servidor rodando.
```sh
python manage.py runserver
```
### Via Navegador:
Podemos acessar as telas via url:
 * Para cadastrar os clientes utilize esse caminho:
   * http://127.0.0.1:8000/clientes/
   
 * Para cadastrar os produtos utilize esse caminho:
   * http://127.0.0.1:8000/produtos/
   
 * Para cadastrar os produtos utilize esse caminho:
   * http://127.0.0.1:8000/favoritos/
   
   
 ### Via API:
  Podemos executar via API:
  
 #### Endpoint de Clientes 
 * Consulta de clientes utilizando metodo GET, retorna todos os clientes cadastros:
  * http://127.0.0.1:8000/api/clients/

 * Para cadastrar clientes utilize metodo POST:
  * http://127.0.0.1:8000/api/clients/
  * Utilize esse exemplo para poder efetuar o cadastro:
   {
        "name": "Rodrigo Ferreira de Araujo",
        "cpf": "414.453.238-37",
        "address": "Rua Malaga, 133",
        "email": "rodferaraujo@gmail",
    }  
    
 * Edição do cadastro de cliente utilize metodo PUT e nesse endpoint podemos cadastrar os produtos favoritos do cliente,
 só precisamos cadastrar um produto para não dar erro de integridade de banco de dados:
  * http://127.0.0.1:8000/api/clients/id/
    {
        "name": "Rodrigo Ferreira de Araujo",
        "cpf": "414.453.238-37",
        "address": "Rua Malaga, 133",
        "email": "rodferaraujo@gmail",
        "favorite": [{"id": 1}, {"id": 2}]
    }  

 * Deletar o registro do cliente só precisa utilizar metodo DELETE:
  * http://127.0.0.1:8000/api/clients/id/
  
 #### Endpoint de Produtos 
 * Consulta de produtos utilizando metodo GET, retorna todos os produtos cadastros:
  * http://127.0.0.1:8000/api/products/
  
 * Para cadastrar os produtos utilize metodo POST:
  * http://127.0.0.1:8000/api/products/
  * Utilize esse exemplo para poder efetuar o cadastro:
   {
        "price": 2079.9,
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTqk8_CUdWLtwvAEz5Ue-ERGsqs-WpjPfnQFpU5oW9TGyBCjVYPIw&usqp=CAc",
        "brand": "Microsoft",
        "title": "Console Xbox One S 1TB Branco",
        "review_score": 0
    }  
    
 * Para editar os produtos utilize metodo PUT:
  * http://127.0.0.1:8000/api/products/id/
  * Utilize esse exemplo para poder efetuar o cadastro:
   {
        "id":1,
        "price": 2079.9,
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTqk8_CUdWLtwvAEz5Ue-ERGsqs-WpjPfnQFpU5oW9TGyBCjVYPIw&usqp=CAc",
        "brand": "Microsoft",
        "title": "Console Xbox One S 1TB Branco",
        "review_score": 0
    }  
  
 * Deletar o registro do produtos só precisa utilizar metodo DELETE:
  * http://127.0.0.1:8000/api/products/id/
