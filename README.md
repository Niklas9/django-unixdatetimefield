django-unixdatetimefield
========================

[![Build Status](https://travis-ci.org/Niklas9/django-unixdatetimefield.svg?branch=master)](https://travis-ci.org/Niklas9/django-unixdatetimefield)
[![Latest Version](https://img.shields.io/pypi/v/django-unixdatetimefield.svg?style=flat) ](https://pypi.python.org/pypi/django-unixdatetimefield/)
[![Downloads](https://pepy.tech/badge/django-unixdatetimefield/week)](https://pepy.tech/project/django-unixdatetimefield)

Provides a UnixDateTimeField for your Django models.

I have found this especially useful when integrating Django into legacy
databases, where the typical DateTime column type is rather stored as a Unix
timestamp (http://en.wikipedia.org/wiki/Unix_time).

UnixDateTimeField is based on the implementation of the standard Django
DateTimeField, making it 100% compatible with all features and options it
supports.

Usage
-----

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

Installation
------------

Install with pip (or easy_install)::

	pip install django-unixdatetimefield

License
-------

BSD, just as the main Django project. See LICENSE file in root of this repo.

Contributing
------------

This project accepts contributions via GitHub pull requests.

* follow Google's Python style guide
  https://google.github.io/styleguide/pyguide.html
* make commits of logical units, messages should include what changed and why
  and be written in past tense
