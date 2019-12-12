#!/usr/bin/env python

import optparse
import sys

import django.conf as conf


if not conf.settings.configured:
    conf.settings.configure(
        DATABASE_ENGINE='django.db.backends.sqlite3',
        DATABASE_NAME='django_unixdatetimefield_test',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'django_unixdatetimefield_test',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django_unixdatetimefield',
            'django_unixdatetimefield.tests',
        ],
        MIDDLEWARE_CLASSES = tuple(),
        ROOT_URLCONF='',
        DEBUG=False,
    )

# NOTE(niklas9):
# * need to have import django_nose after settings has been configured.. I don't
#   like this.. but as it seems to be required by django_nose..
import django_nose

def runtests(*test_args, **kwargs):
    if not test_args:  test_args = ['django_unixdatetimefield']
    import django
    try:
        django.setup()
    except AttributeError:
        pass
    kwargs.setdefault('interactive', False)
    test_runner = django_nose.NoseTestSuiteRunner(**kwargs)
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store',
                      default=1, type=int)
    (options, args) = parser.parse_args()
    runtests(*args, **options.__dict__)
