from django.contrib import admin
from .models import Category, Recipe


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
