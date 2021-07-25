from django.shortcuts import get_object_or_404, render
from .wishlist import Wishlist
from recipe.models import Recipe
from django.http import JsonResponse

# Create your views here.

def wishlist_summary(request):
    return render(request, 'wishlist/summary.html')

def wishlist_add(request):
    wishlist = Wishlist(request)
    if request.POST.get('action') == 'POST':
        recipe_id = int(request.POST.get('recipeId'))
        recipe = get_object_or_404(Recipe, id=recipe_id)
        wishlist.add(recipe = recipe)
        response = JsonResponse({'test': 'data'})
        return response
