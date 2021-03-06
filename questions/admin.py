from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'detail',
    )

    ordering = ('title',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'body',
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
