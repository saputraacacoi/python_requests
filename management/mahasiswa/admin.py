from django.contrib import admin
from orm.models import Mahasiswa

class MahasiswaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Mahasiswa, MahasiswaAdmin)