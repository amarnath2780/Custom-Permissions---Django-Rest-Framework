from django.contrib import admin
from .models import Category, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'category']


@admin.register(Category)
class CategroyAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name']