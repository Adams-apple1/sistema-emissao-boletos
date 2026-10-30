# Sistema de Emissão de Boletos

## Descrição
API REST desenvolvida em Python e Django REST Framework para gerenciamento de emitentes, pagadores e boletos bancários.

O projeto possui uma integração simulada com o Sicoob para demonstrar o fluxo de emissão e evitar registros duplicados.

## Tecnologias
- Python
- Django
- Django REST Framework
- drf-spectacular
- SQLite
- Swagger / OpenAPI

## Como executar

1. Instale as dependências:

   pip install -r requirements.txt

2. Execute as migrações:

   python manage.py migrate

3. Inicie o servidor:

   python manage.py runserver 0.0.0.0:8000

## Documentação da API

Após iniciar o servidor, acesse:

/api/docs/

## Principais endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | /api/emitentes/ | Listar emitentes |
| POST | /api/emitentes/ | Cadastrar emitente |
| GET | /api/pagadores/ | Listar pagadores |
| POST | /api/pagadores/ | Cadastrar pagador |
| GET | /api/boletos/ | Listar boletos |
| POST | /api/boletos/ | Cadastrar boleto |
| POST | /api/boletos/{id}/emitir/ | Simular emissão |

## Regras de negócio

- Um emitente pode possuir vários boletos.
- Um pagador pode possuir vários boletos.
- Cada boleto possui seu próprio status.
- Somente boletos em rascunho podem ser emitidos.
- A emissão duplicada é bloqueada.

## Limitação da integração

A emissão implementada é uma simulação local. Os dados bancários gerados são fictícios e não representam boletos registrados no Sicoob.

A integração real depende de credenciais, certificados e configuração de homologação disponibilizados pela instituição financeira.
