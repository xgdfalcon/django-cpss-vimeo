> ## 🛠 Status: In Development
> django-cpss-vimeo currently in development.

# Python Vimeo API - Django  [<img src="https://github.com/xgdfalcon/django-cpss-vimeo/blob/master/vimeo-django/static/cpss/logo.png?raw=true" alt="CPSS by XGDFalcon®" height="20px" />](https://controlpointsw.com) 

[![Build Status](https://travis-ci.org/xgdfalcon/django-cpss-vimeo.svg?branch=master)](https://travis-ci.org/xgdfalcon/django-cpss-vimeo)
[![PyPI version](https://badge.fury.io/py/django-cpss-vimeo.svg)](https://badge.fury.io/py/django-cpss-vimeo)

## Description

This is the [Django](https://www.djangoproject.com/) component of the
[PyVimeo project](https://github.com/vimeo/vimeo.py),
it implements the needed functionality to integrate
[PyVimeo](https://github.com/vimeo/vimeo.py)
in a Django based project.

## Django version

This project will focus on the currently supported Django releases as
stated on the [Django Project Supported Versions table](https://www.djangoproject.com/download/#supported-versions).

Backward compatibility with unsupported versions won't be enforced.

## Documentation

Project documentation is available at TBP.

## Setup

1. Add "django-cpss-vimeo" to your INSTALLED_APPS setting like this::
```
    INSTALLED_APPS = [
        ...
        'vimeo-django.CPSSVimeoConfig',
    ]
```
2. Include the django-cpss-vimeo URLconf in your project urls.py like this::
```
    path('vimeo/', include('django-cpss-vimeo.urls')),
```
3. Run `python manage.py migrate` to create the django-cpss-vimeo models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/vimeo/ 


## Contributing
See the [CONTRIBUTING.md](CONTRIBUTING.md) document for details.

## Versioning
This project follows [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html).

## License
This project follows the Apache license. See the [LICENSE](LICENSE.md) for details.

