from django.contrib import admin
from .models import Question, Choice

# This is done to make our polls app accessible in the admin page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'published_date', 'published_recently')

    fieldsets = [
        ('Question Information',{ 'fields': ['question_text']} ),
        ('Date Information', {'fields' : ['published_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # To add a filter column in admin page which will be based upon date_published, the type of filter options
    # to display is automatically managed by django, try 'question_text' instead of 'published_date' below

    list_filter = ['published_date']

admin.site.register(Question,QuestionAdmin)
