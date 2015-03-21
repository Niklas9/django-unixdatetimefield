
import datetime
import time

import django.db.models as models


class UnixDateTimeField(models.DateTimeField):

    # TODO(niklas9):
    # * should we take care of transforming between time zones in any way here ?
    # * get default datetime format from settings ?
    DEFAULT_DATETIME_FMT = '%Y-%m-%d %H:%M:%S'
    __metaclass__ = models.SubfieldBase
    description = "Unix timestamp integer to datetime object"

    def get_internal_type(self):
        return 'PositiveIntegerField'

    def to_python(self, val):
        if val is None or isinstance(val, datetime.datetime):
            return val
        if isinstance(val, datetime.date):
            return datetime.datetime(val.year, val.month, val.day)
        return datetime.datetime.fromtimestamp(float(val))

    def get_db_prep_value(self, val, *args, **kwargs):
        if val is None:  return None
        return int(time.mktime(val.timetuple()))

    def value_to_string(self, obj):
        val = self._get_val_from_obj(obj)
        return self.to_python(val).strftime(self.DEFAULT_DATETIME_FMT)
