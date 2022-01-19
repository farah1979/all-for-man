from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_title', 'question_by', 'detail')
    search_fields = ('question_title', 'detail')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
