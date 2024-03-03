
from django.contrib import admin

from .models import Issue
from .models import Comment

admin.site.register(Issue)
admin.site.register(Comment)