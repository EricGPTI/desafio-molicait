# Desafio Molicait API

API que implementa um CRUD em django e persiste os dados no MongoDB.

## Rodando o Projeto Local

Use o [pipenv](https://github.com/pypa/pipenv) para instalar as dependências do projeto.

```
pipenv sync
```

Após instaladas às dependências, ative o ambiente virtual.

```.env
pipenv shell
```

## Variáveis de ambiente
No arquivo **.env** encontram-se as variáveis para o banco de dados da aplicação. Se necessário faça às
alterações. Caso use banco de dados local, mantenha às configurações. 

```.env
DEBUG=False
DB_NAME=molica
DB_HOST=localhost
DB_PORT=27017
```

Setadas às variáveis de ambiente, rode o servidor do Django.

```.django
python manage.py runserver
```
Após o servidor estar ativo, você será direcionado para a página de Pagamentos. 
Trata-se da interface do Django Rest Framework.


## URLs 

Às urls implementadas são:

[Home](http://127.0.0.1:8000)

[Pagamentos](http://127.0.0.1:8000/api/v1/pagamentos)

[Update](http://127.0.0.1:8000/api/v1/pagamento/update/)

[Delete](http://127.0.0.1:8000/api/v1/pagamento/delete/)


## Banco de Dados
Neste projeto foi utilizado MongoDB versão 4.0.

Crie um banco de dado chamado **molica**. Após criado faça o insert do primeiro registro via interface 
do DRF. Após inserir os dados, a collection pagamento será criada e os dados serão persistidos.


## DELETE

A interface do DRF não apresenta um campo content para fazer o insert do id da trasação que 
deseja deletar. Para isso, passe o parâmetro via url da seguinte forma:

```http
http://127.0.0.1:8000/api/v1/pagamento/delete/069cbb62-f87e-4d3a-8d7d-fc251f557f41
```

Após enviar a requisição, se houver um registro com id_pagamento igual ao passado no browser, o registro
será deletado.

As demais urls podem ser testadas diretamente na interface do DRF.
