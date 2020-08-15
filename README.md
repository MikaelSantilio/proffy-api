## Proffy API
---

[![Blog Badge](https://img.shields.io/badge/Cookiecutter%20Django-black?label=built%20with&style=flat&logo=Django&color=12100e)](https://github.com/pydanny/cookiecutter-django/)



| License       | MIT           |
| ------------- |:-------------:|

This is the back-end of the Proffy application.

It's a RESTful API built with Django + PostgreSQL that 
provide the teachers data to the client server.

Online 🌐: https://proffyapi.herokuapp.com/


### Available endpoints
-----------------------


| Method     | Endpoint        | Request                                             | Response                                 |
| ---------- | --------------- | --------------------------------------------------- | ---------------------------------------- |
|  |
| **`GET`**  | `/api/connections/` | `No Body`                                           | `HTTP_200_OK`<br>`{"total": number}` |
| **`POST`** | `/api/connections/` | `{"proffy_user": id}`                               | `HTTP_200_OK`<br>`{"total": number}` |
| **`GET`**  | `/api/classes/`     | `params: {subject, week_day, time}`                                           | `HTTP_200_OK`<br>`[...]`                    |
| **`GET`**  | `/api/classes/`     | `No Body` | `HTTP_200_OK`                            |




### Getting Started
--------------

#### Prerequisites
To run this project in the development mode, you'll need to have a basic environment with Python 3.8.x installed. To use the database, you'll need to have PostgreSQL installed or running on a container.

#### Installing
1. Clone the repository and enter:
```shell
$ git clone https://github.com/MikaelSantilio/proffy-api/

$ cd proffy-api 
```

2. Create a virtualenv:
```shell
$ python3.8 -m venv <virtual env path>
```

3. Activate the virtualenv you have just created:
```shell
$ source <virtual env path>/bin/activate
```

4. Install development requirements:
```shell
$ pip install -r requirements/local.txt
```

5. Set the environment variables:
```
# General
# ------------------------------------------------------------------------------
export DJANGO_DEBUG=True
export DJANGO_ALLOWED_HOSTS=127.0.0.1,0.0.0.0
export CORS_ORIGIN_WHITELIST=127.0.0.1:3000
# PostgreSQL
# ------------------------------------------------------------------------------
export POSTGRES_HOST=<POSTGRES_HOST>
export POSTGRES_PORT=<POSTGRES_PORT>
export POSTGRES_DB=<DB_NAME>
export POSTGRES_USER=<POSTGRES_USER>
export POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
```
> **To help setting up your environment variables, you have a few options**:
> - create an `.env` file in the root of your project and define all the variables you need in it. Then you just need to have `DJANGO_READ_DOT_ENV_FILE=True` in your machine and all the variables will be read.
> - Use a local environment manager like [direnv](https://direnv.net/)

6. Apply migrations:
```shell
$ python manage.py migrate
```

7. Run the development server:
```shell
$ python manage.py runserver 0.0.0.0:8000
```

### License
-----------

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Author
-----------

| [<img src="https://avatars1.githubusercontent.com/u/40041499?s=460&u=b484cfea7185c43f1a07cc8ba3a75a82cdc20b27&v=4" width=100><br><sub>@MikaelSantilio</sub>](https://github.com/MikaelSantilio) |
| :---: |
