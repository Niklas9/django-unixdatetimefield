
import datetime

import django.conf as conf
import django.test as test
import pytz  # 3rd-party timezone lib, required by django already

import django_unixdatetimefield.tests.models as tm
import django_unixdatetimefield.fields as f


class UnixDateTimeFieldTestCase(test.TestCase):

    def test_default_field(self):
        d = datetime.datetime(2015, 2, 21, 19, 38, 32, 209148)
        m = tm.DefaultField.objects.create(created_at=d)
        self.assertTrue(isinstance(m.created_at, datetime.datetime))
        self.assertEqual(m.created_at, d)

    def test_default_field_after_save(self):
        d = datetime.datetime(2015, 2, 21, 19, 38, 32)
        m = tm.DefaultField.objects.create(created_at=d)
        self.assertTrue(isinstance(m.created_at, datetime.datetime))
        self.assertEqual(m.created_at, d)
        m.save()
        self.assertEqual(m.created_at, d)
        # try fetching it again
        n = tm.DefaultField.objects.get()
        self.assertEqual(n.created_at, d)

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

    def test_internal_field_methods_internal_type(self):
        u = f.UnixDateTimeField()
        self.assertEqual(u.get_internal_type(), 'PositiveIntegerField')

    def test_internal_field_methods_to_python_datetime(self):
        u = f.UnixDateTimeField()
        d = datetime.datetime(2019, 9, 19, 19, 19, 19, 191919)
        self.assertEqual(u.to_python(d), d)

    def test_internal_field_methods_to_python_string(self):
        u = f.UnixDateTimeField()
        d = datetime.datetime(2019, 8, 2, 14, 52, 22, 191919)
        d_str = '2019-08-02 14:52:22.191919'
        self.assertEqual(u.to_python(d_str), d)

    def test_internal_field_methods_to_python_unix(self):
        u = f.UnixDateTimeField()
        d = datetime.datetime(2019, 12, 13, 14, 36, 12)
        d_unix_timestamp = 1576269372 #  2019-08-02 14:36:12
        self.assertEqual(u.to_python(d_unix_timestamp), d)

    @test.override_settings(USE_TZ=True, TIME_ZONE='Europe/Stockholm')
    def test_internal_field_methods_to_python_unix_tz(self):
        u = f.UnixDateTimeField()
        d = datetime.datetime(2019, 8, 2, 16, 52, 22)
        d_localized = pytz.timezone('Europe/Stockholm').localize(d)
        d_unix_timestamp = 1564757542 # 2019-08-02 14:52:22 UTC
        self.assertEqual(u.to_python(d_unix_timestamp), d_localized)

    @test.override_settings(USE_TZ=True, TIME_ZONE='Europe/Stockholm')
    def test_default_field_tz(self):
        d = datetime.datetime(2015, 2, 21, 19, 38, 32)
        d_localized = pytz.timezone('Europe/Stockholm').localize(d)
        m = tm.DefaultField.objects.create(created_at=d_localized)
        m.save()
        self.assertEqual(m.created_at, d_localized)

    def test_internal_field_methods_is_string_pos(self):
        u = f.UnixDateTimeField()
        s1 = '2019-08-23 18:00:00'
        self.assertTrue(u._is_string(s1))

    def test_internal_field_methods_is_string_neg(self):
        u = f.UnixDateTimeField()
        i1 = 9
        self.assertFalse(u._is_string(i1))