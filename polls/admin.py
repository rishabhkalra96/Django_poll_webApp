from django.contrib import admin
from .models import Question

# This is done to make our polls app accessible in the admin page
admin.site.register(Question)
