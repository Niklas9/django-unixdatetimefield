
import django.contrib.admin as admin

from .models import MyModel


class MyModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')
	list_filter = ('title', 'created_at')


admin.site.register(MyModel, MyModelAdmin)
