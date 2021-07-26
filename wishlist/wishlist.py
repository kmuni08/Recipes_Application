from recipe.models import Recipe

class Wishlist():
    """
    A base Basket class, providing some default behaviors that can
    be inherited or overrided, as necessary.
    """

# skey is session key
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get('skey')
        if 'skey' not in request.session:
            wishlist = self.session['skey'] = {}
        self.wishlist = wishlist

    def add(self, recipe, qty):
        """
        Adding and updating the users wishlist session data
        """

        recipe_id = str(recipe.id)

        if recipe_id in self.wishlist:
            self.wishlist[recipe_id]['qty'] = qty
        else:
            self.wishlist[recipe_id] = { 'title': str(recipe.title), 'qty': int(qty)}

    
        # self.session.modified = True
        self.save()

    def __iter__(self):
        """
        Collect the recipe_id in the session data to query the database and return recipes.
        """
        recipe_ids = self.wishlist.keys()
        recipes = Recipe.objects.filter(id__in=recipe_ids)
        wishlist = self.wishlist.copy()

        for recipe in recipes:
            wishlist[str(recipe.id)]['recipe'] = recipe

        for item in wishlist.values():
            item['title'] = str(item['title'])
            yield item

    def __len__(self):
        """
        Get the wishlist data and count the qty of items. 
        """
        return sum(item['qty'] for item in self.wishlist.values())


    def delete(self, recipe):
        """
        Delete item from session data
        """
        recipe_id = str(recipe)
        print(recipe_id)
        if recipe_id in self.wishlist:
            del self.wishlist[recipe_id]
            print(recipe_id)
            self.save()

    def save(self):
        self.session.modified = True
