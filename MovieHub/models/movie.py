# models/movie.py
class Movie:
    def __init__(self, title, genre, director, release_year, price):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.price = price

    def __repr__(self):
        return f"Movie({self.title}, {self.genre}, {self.director}, {self.release_year}, {self.price})"
