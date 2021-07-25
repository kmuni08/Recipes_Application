from .wishlist import Wishlist


# This will run every time we have a template opened. 
def wishlist(request):
    return {'wishlist': Wishlist(request)}