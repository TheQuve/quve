from django.contrib import admin

# Register your models here.
from answer.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Answer._meta.fields]
