
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
        self.assertIsNone(m.created_at)

    def test_null_default_field(self):
        d = datetime.datetime(2015, 8, 23, 15, 38, 32, 209198)
        m = tm.NullDefaultField.objects.create()
        self.assertGreater(m.created_at, d)

    def test_blank_field(self):
        # NOTE(niklas9):
        # * blank values for Django field types such as DateTimeField or
        #   ForeignKey will be stored as NULL in the db, hence not asserting
        #   against empty string '' but rather Python's None-type below
        m = tm.BlankField.objects.create()
        self.assertIsNone(m.created_at)

    def test_autoset_field(self):
        m = tm.AutosetField.objects.create()
        self.assertIsNotNone(m.created_at)
        self.assertIsNotNone(m.updated_at)
        self.assertTrue(isinstance(m.created_at, datetime.datetime))
        self.assertTrue(isinstance(m.updated_at, datetime.datetime))
        m.save()
        self.assertGreater(m.updated_at, m.created_at)
