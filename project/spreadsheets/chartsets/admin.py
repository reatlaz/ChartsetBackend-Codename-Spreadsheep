# Register your models here.
from django.contrib import admin
from chartsets.models import Chartset

class ChartsetAdmin(admin.ModelAdmin):
    list_filter = ('userschartsets',)
    list_display = ('name', 'date_modified', 'get_users')
    search_fields = ['name', ]

    def get_users(self, obj):
        return "\n".join([p.username for p in obj.userschartsets.all()])

admin.site.register(Chartset, ChartsetAdmin)