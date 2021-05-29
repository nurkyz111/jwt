from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.App)
class AppAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right',
        'votes'
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_title', 'app']
    list_display = ['question_title', 'app']
    inlines = [
        AnswerInlineModel,
    ]
