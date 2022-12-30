# UniChoose

### [DB Scheme](https://drive.google.com/file/d/1ztxpX7UvMum50ztteePnS10XvCpkbfzM/view?usp=sharing)
### [Website](https://unichoose.ru/)
## -1. Server using
### -1.1 Upload new code from main branch:
```
git pull
docker compose up -d --build
```
### -1.2 Make shortcut:
```
make up
```

## 0. Prerequisites
### 0.1 Installing python:

Download python and install it from official site https://www.python.org/

### 0.2 Cloning git repository:
```
git clone https://github.com/h4x4d/UniChoose.git
```
### 0.3 Going to folder:
```
cd UniChoose
```


### 0.4 If you want to use venv
```
python -m venv venv
```
Windows:
```
.\venv\Scripts\activate
```
Windows with bash:
```
. venv/Scripts/activate
```

Linux:
```
source venv/bin/activate
```


## 1. Fast run project (Install all dependencies and run):
```
make use
```

## 1.0 If you want run docker container
### Just skip first step

## 1.1 Install with poetry (you also need to install poetry to use it)
#### Install only for running project
```
poetry install 
```
Make shortcut:
```
make install
```
#### Install for developing too (Linters and packages to run in dev format included)
```
poetry install --with dev
```
Make shortcut:
```
make install-dev
```


## 1.2 Install with pip (ready to use with default python)
#### Install only for running project
```
pip install -r requirements.txt 
```
Make shortcut:
```
make pip-install
```
#### Install for developing too (Linters included)
```
pip install -r requirements-dev.txt 
```
Make shortcut:
```
make pip-install-dev
```

## 2. Configuring .env

### 2.1 Adding access_key, for example:
```
SECRET_KEY=AYDFHIJUOAIKPLDFFDbi
```
### 2.2 Checking debug status: 1 - on; 0 - off:
```
DEBUG=1
```
### 2.3 Adding allowed hosts, for example:
```
ALLOWED_HOSTS=127.0.0.1 localhost
```
### 2.3 Setting up SQL info, for example:
```
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=iamnotpassword
SQL_HOST=localhost
SQL_PORT=5432
```
### 2.4. If you want to use Docker, you need to set up .env-prod and .env-prod.db:
env-prod
```
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=iamnotpassword
SQL_HOST=db
SQL_PORT=5433
```
env-prod.db
```
POSTGRES_DB=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PASSWORD=iamnotpassword
```

## 3. Running project
### 3.1 If using Docker:
```
docker compose up -d --build
```
Make shortcut:
```
make up
```
### 3.2 If installed with poetry:
```
poetry run python manage.py runserver
```
Make shortcut:
```
make run
```
### 3.1 If installed with pip:
```
python manage.py runserver
```
Make shortcut:
```
make pip-run
```
