# django-xsessions
Middleware that offers session sharing across multiple domains (using the same session backend obviously). Can be used to allow single sign-on across multiple websites.


### Usage

Add django_xsessions to your INSTALLED_APPS and load the XSessionMiddleware
class. Then set the domain names you want to share the session cookie.


```python
MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'xsessions.middleware.XSessionMiddleware', # <------
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xsessions', # <------
)

XSESSION_DOMAINS = ['www.domain1.com', 'www.domain2.com', 'www.domain3.com']
```

You also need to add the xsession_loader to the head section of your base
template.

base.html (or whatever filename you use):

```html
{% load django_xsession %}
<html>
    <head>
        {% xsession_loader %}
    </head>
    <body>
        <h1>hello world</h1>
    </body>
</html>
```
