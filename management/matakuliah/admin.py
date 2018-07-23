from django.contrib import admin
from orm.models import MataPerkuliahan

@admin.register(MataPerkuliahan)
class MataPerkuliahanAdmin(admin.ModelAdmin):
    pass