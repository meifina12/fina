from django.contrib import admin
from .models import Jenis_Hewan, Hewan
# Register your models here.


class Jenis_HewanAdmin(admin.ModelAdmin):
    list_display = ("Jenis_Hewan", "Makanan_Hewan",)


admin.site.register(Jenis_Hewan, Jenis_HewanAdmin)
admin.site.register(Hewan)
