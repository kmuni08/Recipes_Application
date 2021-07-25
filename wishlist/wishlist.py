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

    def add(self, recipe):
        """
        Adding and updating the users wishlist session data
        """

        recipe_id = recipe.id
        if recipe_id not in self.wishlist:
            self.wishlist[recipe_id] = { 'title': str(recipe.title)}

        self.session.modified = True