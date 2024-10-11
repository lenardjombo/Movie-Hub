# models/user.py
class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.rented_movies = []
        self.purchased_movies = []

    def rent_movie(self, movie):
        self.rented_movies.append(movie)

    def purchase_movie(self, movie):
        self.purchased_movies.append(movie)

    def __repr__(self):
        return f"User({self.username}, Admin: {self.is_admin})"
