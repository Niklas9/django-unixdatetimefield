
import datetime

import django.test as test
import django_unixdatetimefield.tests.models as tm


class UnixDateTimeFieldTestCase(test.TestCase):

    def test_default_field(self):
        d = datetime.datetime(2015, 2, 21, 19, 38, 32, 209148)
        m = tm.DefaultField.objects.create(created_at=d)
        self.assertTrue(isinstance(m.created_at, datetime.datetime))
        self.assertEqual(m.created_at, d)

    def test_null_field(self):
        m = tm.NullField.objects.create()
        self.assertEqual(m.created_at, None)

    def test_autoset_field(self):
        m = tm.AutosetField.objects.create()
        self.assertNotEqual(m.created_at, None)
        self.assertNotEqual(m.updated_at, None)
        self.assertTrue(isinstance(m.created_at, datetime.datetime))
        self.assertTrue(isinstance(m.updated_at, datetime.datetime))
        m.save()
        self.assertGreater(m.updated_at, m.created_at)
