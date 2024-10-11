# Services/rental_service.py
import json

def rent_movie(user, movie):
    user.rent_movie(movie)
    save_transaction(user, movie, "rent")

def save_transaction(user, movie, transaction_type):
    transaction = {
        'username': user.username,
        'movie': movie.title,
        'transaction_type': transaction_type
    }
    with open('data/transactions.json', 'a') as f:
        f.write(json.dumps(transaction) + "\n")
