# models/cart.py
class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, movie):
        self.items.append(movie)

    def remove_from_cart(self, movie):
        if movie in self.items:
            self.items.remove(movie)

    def clear_cart(self):
        self.items = []

    def __repr__(self):
        return f"Cart({self.items})"
