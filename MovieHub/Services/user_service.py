# Services/user_service.py
import json
def register_user(store, username, password, is_admin=False):
    user = User(username, password, is_admin)
    store.users.append(user)
    save_users(store.users)

def login_user(store, username, password):
    for user in store.users:
        if user.username == username and user.password == password:
            return user
    return None

def save_users(users):
    with open('data/users.json', 'w') as f:
        json.dump([user.__dict__ for user in users], f, indent=4)

def load_users():
    with open('data/users.json', 'r') as f:
        return json.load(f)
