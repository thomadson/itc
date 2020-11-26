from django.contrib import admin
from .models import Formations

# Register your models here.
class FormationsAdmin(admin.ModelAdmin):
    list_display = ('lib_fomration','module_formation')

admin.site.register(Formations,FormationsAdmin)

