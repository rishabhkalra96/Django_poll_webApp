from django.contrib import admin
from .models import Question, Choice

# This is done to make our polls app accessible in the admin page
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Information',{ 'fields': ['question_text']} ),
        ('Date Information', {'fields' : ['published_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
