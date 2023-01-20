from django.contrib import admin

from main.models import SomeString


@admin.register(SomeString)
class SomeStringAdmin(admin.ModelAdmin):
    pass
