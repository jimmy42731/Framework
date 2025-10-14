from django.contrib import admin
from .models import Warga
from .models import Pengaduan

# Register your models here.
admin.site.register(Warga)
admin.site.register(Pengaduan)