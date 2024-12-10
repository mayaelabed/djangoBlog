from django.contrib import admin
from .models import BlogPost, Comment

# Registering BlogPost and Comment Models
admin.site.register(BlogPost)
admin.site.register(Comment)
