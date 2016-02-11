from __future__ import unicode_literals

from django.db import models

from django_unixdatetimefield import UnixDateTimeField


class MyModel(models.Model):
        title = models.CharField(max_length=100)
        created_at = UnixDateTimeField()

    
