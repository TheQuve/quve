from django.contrib import admin

# Register your models here.
from question.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]
