# Define dictionary of movies and their information
movies = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}

# Print out the movies and their information using square bracket syntax and .keys and .values
for movie in movies:
    print(f"Movie: {movie}")
    for key, value in movies[movie].items():
        print(f"{key}: {value}")
    print()

# Update an element in the dictionary
movies["The Dark Knight"]["year"] = 2009

# Delete an element from the dictionary
del movies["Pulp Fiction"]

# Get a value from the dictionary using .get
genre = movies.get("Inception").get("genre")
print(f"The genre of Inception is {genre}.")


import json
import os

DATA_FILE = "movies.json"

# -----------------------------
#  Load & Save
# -----------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(movies):
    with open(DATA_FILE, "w") as f:
        json.dump(movies, f, indent=4)


# -----------------------------
#  Add Movie
# -----------------------------
def add_movie(movies):
    print("\n--- Add a New Movie ---")
    title = input("Title: ").strip()

    if title in movies:
        print("Movie already exists.\n")
        return

    genre = input("Genre: ").strip()
    director = input("Director: ").strip()
    year = input("Release Year: ").strip()

    # Data validation
    if not year.isdigit():
        print("Year must be a number.\n")
        return

    actors = input("Actors (comma separated): ").split(",")
    actors = [a.strip() for a in actors]

    movies[title] = {
        "genre": genre,
        "director": director,
        "year": year,
        "actors": actors
    }

    print("Movie added successfully!\n")


# -----------------------------
#  Edit Movie
# -----------------------------
def edit_movie(movies):
    print("\n--- Edit a Movie ---")
    title = input("Enter movie title to edit: ").strip()

    if title not in movies:
        print("Movie not found.\n")
        return

    movie = movies[title]

    print("Leave blank to keep current value.\n")

    new_genre = input(f"Genre ({movie['genre']}): ").strip() or movie['genre']
    new_director = input(f"Director ({movie['director']}): ").strip() or movie['director']
    new_year = input(f"Year ({movie['year']}): ").strip() or movie['year']

    if not new_year.isdigit():
        print("Year must be a number.\n")
        return

    new_actors = input("Actors (comma separated, blank to keep): ").strip()
    if new_actors:
        new_actors = [a.strip() for a in new_actors.split(",")]
    else:
        new_actors = movie["actors"]

    movies[title] = {
        "genre": new_genre,
        "director": new_director,
        "year": new_year,
        "actors": new_actors
    }

    print("Movie updated successfully!\n")


# -----------------------------
#  Delete Movie
# -----------------------------
def delete_movie(movies):
    print("\n--- Delete a Movie ---")
    title = input("Enter movie title to delete: ").strip()

    if title in movies:
        del movies[title]
        print("Movie deleted.\n")
    else:
        print("Movie not found.\n")


# -----------------------------
#  View All Movies
# -----------------------------
def view_movies(movies):
    print("\n--- All Movies ---")

    if not movies:
        print("No movies in the database.\n")
        return

    for title, info in movies.items():
        print(f"\nTitle: {title}")
        print(f"  Genre: {info['genre']}")
        print(f"  Director: {info['director']}")
        print(f"  Year: {info['year']}")
        print(f"  Actors: {', '.join(info['actors'])}")

    print()


# -----------------------------
#  Search Movies
# -----------------------------
def search_movies(movies):
    print("\n--- Search Movies ---")
    term = input("Enter search term: ").lower().strip()

    found = False

    for title, info in movies.items():
        if (term in title.lower() or
            term in info["genre"].lower() or
            term in info["director"].lower() or
            term in info["year"].lower() or
            any(term in actor.lower() for actor in info["actors"])):

            print(f"\nTitle: {title}")
            print(f"  Genre: {info['genre']}")
            print(f"  Director: {info['director']}")
            print(f"  Year: {info['year']}")
            print(f"  Actors: {', '.join(info['actors'])}")
            found = True

    if not found:
        print("No matching movies found.\n")


# -----------------------------
#  Menu System
# -----------------------------
def main():
    movies = load_data()

    while True:
        print("=== Movie Database Menu ===")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View All Movies")
        print("5. Search Movies")
        print("6. Save & Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            edit_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            view_movies(movies)
        elif choice == "5":
            search_movies(movies)
        elif choice == "6":
            save_data(movies)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()

