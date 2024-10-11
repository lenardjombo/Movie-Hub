#Main entry point of the application
# app.py
from models.store import Store
from models.movie import Movie
from models.user import User
from services.movie_service import add_movie, find_movie
from services.user_service import register_user, login_user
from services.rental_service import rent_movie
from services.purchase_service import purchase_movie
from utils.payment import process_payment

def main():
    store = Store()

    while True:
        print("\nMovie Store System")
        print("1. Register")
        print("2. Login")
        print("3. Add Movie (Admin)")
        print("4. Rent Movie")
        print("5. Purchase Movie")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(store, username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login_user(store, username, password)
            if user:
                print(f"Welcome, {user.username}")
            else:
                print("Invalid credentials")

        elif choice == "3":
            title = input("Enter movie title: ")
            genre = input("Enter genre: ")
            director = input("Enter director: ")
            release_year = input("Enter release year: ")
            price = float(input("Enter price: "))
            movie = Movie(title, genre, director, release_year, price)
            add_movie(store, movie)

        elif choice == "4":
            title = input("Enter the movie title you want to rent: ")
            movie = find_movie(store, title)
            if movie:
                print(f"Renting {movie.title}")
                rent_movie(user, movie)
            else:
                print("Movie not found")

        elif choice == "5":
            title = input("Enter the movie title you want to purchase: ")
            movie = find_movie(store, title)
            if movie:
                print(f"Purchasing {movie.title}")
                if process_payment(movie.price):
                    purchase_movie(user, movie)
            else:
                print("Movie not found")

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
