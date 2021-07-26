from django.shortcuts import get_object_or_404, render
from .wishlist import Wishlist
from recipe.models import Recipe
from django.http import JsonResponse

# Create your views here.

def wishlist_summary(request):
    wishlist = Wishlist(request)
    return render(request, 'wishlist/summary.html', {'wishlist': wishlist})

def wishlist_add(request):
    wishlist = Wishlist(request)
    if request.POST.get('action') == 'POST':
        recipe_id = int(request.POST.get('recipeId'))
        recipe_qty = 1
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # if recipe_id not in wishlist:
        #     wishlist.add(recipe = recipe, qty = recipe_qty)
        wishlist.add(recipe = recipe, qty = recipe_qty)
        # response = JsonResponse({'test': 'data'})
        # wishlistqty = wishlist.__len__()
        wishlistqty = wishlist.__len__()
        response = JsonResponse({'qty': wishlistqty})
        return response

def wishlist_delete(request):
    wishlist = Wishlist(request)
    if request.POST.get('action') == 'POST':
        print("recipe_id", request.POST.get('recipeId'))
        
        recipe_id = int(request.POST.get('recipeId'))
    
        wishlist.delete(recipe=recipe_id)

        wishlistqty = wishlist.__len__()
        response = JsonResponse({'qty': wishlistqty})
        return response

