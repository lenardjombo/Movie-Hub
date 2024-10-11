# Services/purchase_service.py
import json

def purchase_movie(user, movie):
    user.purchase_movie(movie)
    save_transaction(user, movie, "purchase")

def save_transaction(user, movie, transaction_type):
    transaction = {
        'username': user.username,
        'movie': movie.title,
        'transaction_type': transaction_type
    }
    with open('data/transactions.json', 'a') as f:
        f.write(json.dumps(transaction) + "\n")
