# Nosso Sisu Django

Nosso Sisu Django é uma aplicação web construída com Django para simular e gerenciar uma versão simplificada do SISU (Sistema de Seleção Unificada) utilizado para ingressar em universidades federais por todo o Brasil.

## Funcionalidades

- Registro e autenticação de usuários
- Gerenciamento de cursos e universidades
- Envio de inscrições e sistema de classificação
- Painel administrativo para gerenciamento de dados
- Cache de dados de API de Geocode para mostrar a localização das universidades

## Requisitos

- Possuir o **python** em seu computador
- Possuir o **redis** instalado para armazenar o cache

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/matheus-q14/Nosso-Sisu-Django.git
    ```

2. Entre no diretório, crie e ative um ambiente virtual:
    ```bash
    cd nosso-sisu-django
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
5. Crie o arquivo `.env` e adicione a variáveis de ambiente

    ```bash
    # Secret key django
    SECRET_KEY="crie-uma-string-com-caracteres-aleatorios" # Não compartilhe com ninguém

    # Redis db cache
    REDIS_USER="seu-usuario-redis"
    REDIS_PASSWORD="senha-do-usuario-redis"

    # Debug
    DEBUG="True/False" # Em desenvolvimento use True e em produção use False
    ```

6. Crie um super usuário para gerenciar seu sistema
    
    ```bash
    python3 manage.py createsuperuser
    ```

7. Execute o servidor de desenvolvimento:
    ```bash
    python3 manage.py runserver
    ```

## Uso

1. Acesse a aplicação em `http://127.0.0.1:8000/`.
2. Registre-se como um novo usuário ou faça login com credenciais existentes.
3. Explore as funcionalidades para gerenciar cursos, universidades e inscrições.


## Licença

Este projeto está licenciado sob a Licença MIT.

## Contato

Para dúvidas ou sugestões, entre em contato com o mantenedor do projeto em `matheusquerino91#@gmail.com`.