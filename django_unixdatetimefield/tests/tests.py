
import datetime

import django.test as test
import django_unixdatetimefield.tests.models as tm


class UnixDateTimeFieldTestCase(test.TestCase):

    def test_default_field(self):
        d = datetime.datetime(2015, 2, 21, 19, 38, 32, 209148)
        m = tm.DefaultField.objects.create(created_at=d)
        assert m.created_at == d

    def test_null_field(self):
        m = tm.NullField.objects.create()
        assert m.created_at == None

    def test_autoset_field(self):
        m = tm.AutosetField.objects.create()
        assert not m.created_at == None
        assert not m.updated_at == None
        assert type(m.created_at) == datetime.datetime
        assert type(m.updated_at) == datetime.datetime
        m.save()
        assert m.updated_at > m.created_at
