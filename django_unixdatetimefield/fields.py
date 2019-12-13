import datetime
import time

import django.conf as conf
import django.db.models as models
import django.utils as utils
import pytz


class UnixDateTimeField(models.DateTimeField):

    description = "Unix timestamp integer to datetime object"

    def get_internal_type(self):
        return 'PositiveIntegerField'

    def to_python(self, val):
        if val is None or isinstance(val, datetime.datetime):
            return val
        if isinstance(val, datetime.date):
            return datetime.datetime(val.year, val.month, val.day)
        elif self._is_string(val):
            return utils.dateparse.parse_datetime(val)
        else:
            datetime_value = datetime.datetime.fromtimestamp(int(val))
            if conf.settings.USE_TZ:
                return utils.timezone.make_aware(datetime_value,
                            timezone=pytz.timezone(conf.settings.TIME_ZONE))
            else:
                return datetime_value

    def _is_string(self, val):
        try:
            if isinstance(val, unicode):  # Python 2.7 compatibility support
                return True
        except:
            pass
        return isinstance(val, str)

    def get_db_prep_value(self, val, *args, **kwargs):
        if val is None:
            if self.default == models.fields.NOT_PROVIDED:  return None
            return self.default
        return int(time.mktime(val.timetuple()))

    def value_to_string(self, obj):
        val = self._get_val_from_obj(obj)
        return self.to_python(val).strftime(conf.settings.DATETIME_FORMAT)

    def from_db_value(self, val, *args, **kwargs):
        return self.to_python(val)
