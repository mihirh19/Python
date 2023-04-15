# Django Web Application

This is a Django web application that serves as a simple example of various features and functionalities of Django. It
covers the following topics:

- [Project Setup](#project-setup)
- [Models and Database](#models-and-database)
- [Views and URL Routing](#views-and-url-routing)
- [Templates and Front-end](#templates-and-front-end)
- [Authentication and Authorization](#authentication-and-authorization)
- [Static and Media Files](#static-and-media-files)
- [Testing](#testing)

## Project Setup

To run this Django web application, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install Django using `pip install django`.
4. Navigate to the project directory and run `python manage.py migrate` to apply database migrations.
5. Start the development server using `python manage.py runserver`.
6. Open a web browser and go to `http://localhost:8000/` to see the home page of the web application.

## Models and Database

Models in Django are used to define the structure of your database tables. You can define your models as Python classes,
and Django will automatically create the corresponding database tables for you. Here's an example of a model definition:

```python
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
```

This model defines a Person with three fields: first_name, last_name, and age. The CharField and IntegerField are
examples of different field types that you can use in your models.

## Views and Templates

Views in Django are responsible for handling HTTP requests and returning HTTP responses. A view can render a template,
which is a text file that defines the structure and layout of the HTML that will be sent to the client. Here's an
example of a view that renders a template:

```python
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
```

This view renders the `home.html` template and returns the resulting HTML to the client.

## URL Routing

URL routing in Django is done using URL patterns. You can define URL patterns in your `urls.py` file, which is typically
located in your project's root directory. Here's an example of a URL pattern:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

This URL pattern maps the root URL (`/`) to the `home` view, which we defined earlier.

## Forms

Forms in Django are used to handle user input and validate data. You can define your forms as Python classes, and Django
provides various form fields that you can use to build your forms. Here's an example of a form definition:

```python
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
```

This form definition defines a `LoginForm` with two fields: `username` and `password`. The `CharField` is used to define
a
text
input field, and the `PasswordInput` widget is used to render the password field as a password input.

## Authentication and Authorization

Django provides built-in authentication and authorization functionality to handle user authentication and authorization.
You can use Django's built-in authentication views and middleware to handle user authentication, and decorators to
handle authorization. Here's an example of how to use Django's authentication views and decorators:

```python
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')
```

In this example, the `login_view` is a view that handles user login. It uses Django's built-in `authenticate()` and
`login()`
functions to authenticate the user and log them in. The `login_required` decorator is used to ensure that the `home`
view
can only be accessed by logged-in users.

## Static Files

Static files in Django, such as CSS, JavaScript, and images, are typically stored in a static directory within your app
or project. You can define static files in your templates using the `{% static %}` template tag, and serve them using
Django's built-in static view. Here's an example of how to serve static files in Django:

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

```html
# home.html
<!DOCTYPE html>
<html>
<head>
    <title>My Web App</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
<!-- HTML content goes here -->
<script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

n this example, the `STATIC_URL` setting is configured to `/static/`, and the `STATICFILES_DIRS` setting is used to
specify
the location of the static files. The `{% static %}` template tag is used to generate the URL for the static files in
the
templates.

## Middleware

Middleware in Django is a way to process requests and responses globally before they reach the view or after they leave
the view. Middleware can be used for various purposes, such as authentication, caching, and logging. Here's an example
of how to define middleware in Django:

```python
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed before the view
        response = self.get_response(request)
        # Code to be executed after the view
        return response
```

In this example, `MyMiddleware` is a custom middleware that can be defined in your project. The `__init__` method is
used
to
initialize the middleware, and the `__call__` method is called for each request. You can add your custom logic before
and
after the view processing in the `__call__` method. To use this middleware, add it to the `MIDDLEWARE` setting in your
Django project's `settings.py` file:

```python
# settings.py
MIDDLEWARE = [
    # other middleware...
    'myapp.middleware.MyMiddleware',  # Add your middleware here
]
```
