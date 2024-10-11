# Services/movie_service.py
import json

def load_movies():
    with open('data/movies.json', 'r') as f:
        return json.load(f)

def save_movies(movies):
    with open('data/movies.json', 'w') as f:
        json.dump([movie.__dict__ for movie in movies], f, indent=4)

def add_movie(store, movie):
    store.add_movie(movie)
    save_movies(store.movies)

def find_movie(store, title):
    return store.find_movie(title)
