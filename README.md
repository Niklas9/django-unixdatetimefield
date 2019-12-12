# django-unixdatetimefield

[![Build Status](https://travis-ci.org/Niklas9/django-unixdatetimefield.svg?branch=master)](https://travis-ci.org/Niklas9/django-unixdatetimefield)
[![Latest Version](https://img.shields.io/pypi/v/django-unixdatetimefield.svg?style=flat) ](https://pypi.python.org/pypi/django-unixdatetimefield/)
[![Downloads](https://pepy.tech/badge/django-unixdatetimefield/week)](https://pepy.tech/project/django-unixdatetimefield)

Provides a UnixDateTimeField for your Django models. Now with Django 3 support as well.

I have found this especially useful when integrating Django into legacy
databases, where the typical DateTime column type is rather stored as a Unix
timestamp (http://en.wikipedia.org/wiki/Unix_time).

UnixDateTimeField is based on the implementation of the standard Django
DateTimeField, making it 100% compatible with all features and options it
supports.


## Usage

First you'll need to attach a UnixDateTimeField to your model. This acts as a
the equivalence of a Django PositiveIntegerField at the database level but
provides a Django DateTimeField at the ORM abstraction layer.

Example model:

	from django_unixdatetimefield import UnixDateTimeField

	class MyModel(models.Model):
		created_at = UnixDateTimeField()

Python ORM query:

    >>> m = MyModel()
    >>> m.created_at = datetime.datetime(2015, 2, 21, 19, 38, 32, 209148)
    >>> m.save()

Database:

    sqlite> select created_at from mymodel;
    1426967129

Enjoy!


## Installation

Install with pip:

	pip install django-unixdatetimefield


## Compatibility
Current support matrix (routinely tested for for each release, see `.travis.yml` for more details):

* Django 1.11.x with Python 2.7, 3.4, 3.5
* Django 2.0.x with Python 3.4
* Django 2.x.y with Python 3.5
* Django 2-3.x with Python 3.6, 3.7, 3.8

As the main use-case of this library is to integrate with legacy databases -- I'm keen to keep older versions of Python and Django supported. Let me know if you're using a combination that's not supported, and I'll be happy to try to see if we can support it.

I acknowledge though, and respect, the ones who prefer using unix timestamps in their databases, but in my experience those devs are increasingly becoming fewer and fewer :)


## Contributing
This project accepts contributions via GitHub pull requests.

* follow Google's Python style guide
  https://google.github.io/styleguide/pyguide.html
* make commits of logical units, messages should include what changed and why
  and be written in past tense

### Testing
The easiest way I've found to test the different mixes of Python and Django
versions has been to use Docker, with simple flags to boot up with e.g. Python 2.7
or 3.8, and e.g. Django 1.11.x or Django 3.x. For anyone who wants to test or contribute, I believe this is the fastest way.
There's a helperfile named `build_n_run.sh` that will build the docker image and spin up a container automatically.

### Uploading to pypi
In general,  I think this guide is pretty useful -- https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications.
As all settings are setup in this project already, it should simply be to

  1. `$ python3 setup.py sdist`
  2. `$ python3 setup.py sdist upload`

remember to update the verion numbers in `setup.py` and `django_unixdatetimefield/__init__.py` beforehand.


## License
BSD, just as the main Django project. Please see `LICENSE` file in root of this repo.
