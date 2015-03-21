django-unixdatetimefield
------------------------

Provides a UnixDateTimeField to your Django models.

Installation
============

Install it with pip (or easy_install)::

	pip install django-unixdatetimefield

Usage
=====

First you'll need to attach a UnixDateTimeField to your model. This acts as a
the equivalence of a Django PositiveIntegerField on the database level but
provides a Django DateTimeField at the ORM abstraction layer. Example::

	from django_unixdatetimefield import UnixDateTimeField

	class MyModel(models.Model):
		created_at = UnixDateTimeField()

Check out the source for more configuration values.

Enjoy!

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
