from django.contrib import admin
from .models import Personnels

# Register your models here.
class PersonnelsAdmin(admin.ModelAdmin):
    list_display = ('identite','poste')

admin.site.register(Personnels,PersonnelsAdmin)
