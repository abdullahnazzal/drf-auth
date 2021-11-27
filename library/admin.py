from django.contrib import admin
from django.db.models.base import Model
from .models import Book
# Register your models here.
admin.site.register(Book)