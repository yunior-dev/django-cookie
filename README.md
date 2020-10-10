# Django Cookiecutter

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Django-Cookie is a template for jumpstarting production-ready Django projects quickly.

My version is inspire by Daniel Roy Greenfeld's [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) and the [Laravel-Mix](https://github.com/JeffreyWay/laravel-mix) package. I also integrated [Vue.js](https://vuejs.org) as the frontend and [tailwindcss](https://tailwindcss.com) for styling similar to the [Laravel UI](https://github.com/laravel/ui). These features are easy to change or remove.

My primary purpose for creating this cookiecutter is for the use of projects where I want to use a javascript framework i.e. Vue.js and Django on the back end especially to use Django's built-in admin panel.

## Features

---

- For Django 3.1
- Works with Python 3.8
- Uses PostgreSQL or SQLite3
- Vue.js 2.6
- Tailwindcss 1.8
- Includes the preview version of [@tailwindcss/ui](https://tailwindui.com/?utm_source=tailwindcss&utm_medium=footer-banner) 0.6.2
- Uses [django-rest-framework](https://www.django-rest-framework.org/)
- Optional basic ASGI setup for Websockets
- Optional custom static with [Laravel-Mix](https://github.com/JeffreyWay/laravel-mix) and [Django Mix](https://pypi.org/project/djangomix/)
- Optional use of [Docker](https://hub.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/)

## Usage

---

First make sure you have [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html#install-cookiecutter) installed globally:

```
pip install --user cookiecutter
```

or

```
pip3 install cookiecutter
```

Now run it against this repo:

```
cookiecutter https://github.com/yespinal/django-vue-cookie
```
