from django.contrib import admin
from .models import Subject
from .models import Comment

# Register your models here.
admin.site.register(Subject)

admin.site.register(Comment)