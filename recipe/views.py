from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Category, Recipe
from django.http import JsonResponse


def all_recipes(request):
    totalrecipes = Recipe.objects.all() # Select all from recipes (equivalent in SQL)
    print("recipes", totalrecipes)
    return render(request, 'recipe/home.html', {'recipes': totalrecipes})

def recipe_detail(request, slug):
    # get individual item from db. 
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/detail.html', {
        'recipe': recipe
    })

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    recipes = Recipe.objects.filter(category = category)
    return render(request, 'recipes/category.html', {'category': category, 'recipes': recipes})