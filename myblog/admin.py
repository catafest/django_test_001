from django.contrib import admin
# Register your models here.
from .models import Post
# Post over time
from django.db.models.functions import Trunc
from django.db.models import DateTimeField

admin.site.register(Post)
