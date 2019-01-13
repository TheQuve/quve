from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in models.Category._meta.fields
    ]


@admin.register(models.CategoryMapping)
class CategoryMappingAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in models.CategoryMapping._meta.fields
    ]
