## Simple Django Cookiecutter Template

Will create Django 5 project with predefined packages, apps structure and uvicorn as web dev server.

## Project Structure

```shell
├── apps
│   ├── __init__.py
├── api
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       └── urls.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings
│   └── wsgi.py
├── docker-compose.yml
├── Makefile
├── manage.py
├── requirements.in
├── requirements.txt
```

## Predefined packages

Template uses `pip-tools` with the following `requirements.in`

```shell
Django
djangorestframework
django-environ
psycopg2-binary
django-environ
pytest-django
drf-spectacular
pytest-coverage
uvicorn
pre-commit
```

## Database

Template contains simple `docker-compose.yml` with PostgreSQL database and no password login

```
version: '3'


services:
  postgres:
    image: postgres:13-alpine
    ports:
      - 5432:5432
    environment:
      - POSTGRES_HOST_AUTH_METHOD=trust
```

And credentials are stored in `.env` file 

```shell
DATABASE_URL=postgres://postgres@localhost/postgres
```

## Quick start

```shell
cookiecutter https://github.com/lexluter1988/cookiecutter-django.git

cd <chosen project name>
python3.10 -m venv venv
source venv/bin/activate
pip install pip-tools
pip install cookiecutter

make deps
python manage.py collectstatics
python manage.py migrate
```
