django-unixdatetimefield
------------------------

Provides a UnixDateTimeField to represent date and time stored as
Unix time, http://en.wikipedia.org/wiki/Unix_time, at the database level.

I have found it useful quite often when working with legacy systems.

Usage
=====

First you'll need to attach a UnixDateTimeField to your model. This acts as a
the equivalence of a Django PositiveIntegerField at the database level but
provides a Django DateTimeField at the ORM abstraction layer.

Example model::

	from django_unixdatetimefield import UnixDateTimeField

	class MyModel(models.Model):
		created_at = UnixDateTimeField()

Python ORM query::

    >>> m = MyModel()
    >>> m.created_at = datetime.datetime(2015, 2, 21, 19, 38, 32, 209148)
    >>> m.save()

Database::

    sqlite> select created_at from mymodel;
    1426967129

Installation
============

Install it with pip (or easy_install)::

	pip install django-unixdatetimefield

License
=======

BSD, just as the main Django project. See LICENSE file in root of this repo.

Contributing
============

This project accepts contributions via GitHub pull requests.

* follow Google's Python style guide
  https://google-styleguide.googlecode.com/svn/trunk/pyguide.html 
* make commits of logical units, messages should include what changed and why
  and be written in past tense
