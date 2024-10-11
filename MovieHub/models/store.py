# models/store.py
class Store:
    def __init__(self):
        self.movies = []  # List to hold all the movies in the store
        self.users = []   # List to hold all the users accounts (Registered users)

    def add_movie(self, movie):
        self.movies.append(movie)  # Add movie to the store's inventory

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None
