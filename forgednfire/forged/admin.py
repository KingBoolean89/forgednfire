from django.contrib import admin
from .models import Forged

# Register your models here.
class ForgedAdmin(admin.ModelAdmin):
    list_display = ['name', 'length', 'createdAt']

admin.site.register(Forged,ForgedAdmin)
