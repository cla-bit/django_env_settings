# Django Environment Settings

--------------

This is a Django configuration settings for various environments such as development/local, 
staging and production.


This aids a simple and fast setup while implementing security for django/django 
restframework applications especially when deploying to a production environment.


> **NOTE**
> 
> This works for a general django/django restframework application.
> If using django restframework, install the required dependencies and setup accordingly.


> **TIP**
> 
> This project uses "poetry" to manage dependencies. Ensure you have "poetry" already installed.
> 
> Read documentation here on how to install "poetry": https://python-poetry.org/docs/
>
> You can still use "pip" to install the dependencies in the *requirements.txt* file

----------

## Project Structure

```text

└── root/
    ├── loggings/  # implements logging for the various environments
    │   ├── __init__.py
    │   ├── base.py
    │   ├── local.py
    │   ├── production.py
    │   └── staging
    ├── manage.py
    ├── pyproject.toml
    ├── ruff.toml  # linting
    └── settings/
        ├── libs_config/  # directory for third-party libraries such as celery
        │   └── __init__.py
        ├── __init__.py
        ├── asgi.py
        ├── env.py
        ├── urls.py
        ├── wsgi.py
        └── config/  # django configuration directory
            ├── __init__.py
            ├── base.py
            ├── local.py
            ├── production.py
            └── staging.py

```

------------

## Installation & Setup


#### Installation

- Clone the repository

```git
git clone https://github.com/cla-bit/django_env_settings.git
cd <your_project>
```

- Create your virtual environment

```shell
python -m venv <your_venv>
```
> **NOTE**
> 
> If using linux/MacOS based terminals, use "python3".

- Activate your virtual environment

```shell
<your_venv>\Scripts\activate
```

*Linux/MacOS terminals*
```shell
source <your_venv>/bin/activate
```

- Install the dependencies using *poetry* or *pip*

```shell
poetry install
```

or using pip

```shell
pip install -r requirements.txt
```
