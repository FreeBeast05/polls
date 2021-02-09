from django.contrib import admin

from .models import Question, Choice, Polls_table

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Polls_table)

