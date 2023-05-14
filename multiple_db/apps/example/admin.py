from django.contrib import admin

from .models import ExampleModel
# Register your models here.


class ExampleAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    
    
admin.site.register(ExampleModel, ExampleAdmin)
