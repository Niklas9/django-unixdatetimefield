
import datetime

import django.db.models as models

import django_unixdatetimefield


class DefaultField(models.Model):
    created_at = django_unixdatetimefield.UnixDateTimeField()

class BlankField(models.Model):
    created_at = django_unixdatetimefield.UnixDateTimeField(null=True, blank=True)

class NullField(models.Model):
    created_at = django_unixdatetimefield.UnixDateTimeField(null=True)

class NullDefaultField(models.Model):
    created_at = django_unixdatetimefield.UnixDateTimeField(null=True,
                                            default=datetime.datetime.utcnow())

class AutosetField(models.Model):
    created_at = django_unixdatetimefield.UnixDateTimeField(auto_now_add=True)
    updated_at = django_unixdatetimefield.UnixDateTimeField(auto_now=True)
