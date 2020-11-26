from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display=('titre','description')

admin.site.register(Services,ServicesAdmin)
# Register your models here.
