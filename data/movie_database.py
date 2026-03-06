import xml.etree.ElementTree as ET

def xml_to_dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    movie_db = {}

    for genre in root.findall('genre'):
        genre_name = genre.get('category')
        movie_db[genre_name] = {}

        for decade in genre.findall('decade'):
            decade_years = decade.get('years')
            movie_db[genre_name][decade_years] = []

            for movie in decade.findall('movie'):
                movie_info = {
                    "title": movie.get("title"),
                    "favorite": movie.get("favorite"),
                    "format": movie.find("format").text.strip(),
                    "year": movie.find("year").text.strip(),
                    "rating": movie.find("rating").text.strip(),
                    "description": movie.find("description").text.strip()
                }
                movie_db[genre_name][decade_years].append(movie_info)

    return movie_db

movie_dict = xml_to_dict("movie.xml")
# print(movie_dict)   # temporary, just to verify


def view_movies():
    for genre, decades in movie_dict.items():
        print(f"\nGenre: {genre}")
        for decade, movies in decades.items():
            print(f"  Decade: {decade}")
            for m in movies:
                print(f"    - {m['title']} ({m['year']})")
movie_dict = xml_to_dict("movie.xml")

# # TEMPORARY: test view_movies()
# view_movies()


import xml.etree.ElementTree as ET
import json

# ---------------- XML → Dictionary ----------------

def xml_to_dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    movie_db = {}

    for genre in root.findall('genre'):
        genre_name = genre.get('category')
        movie_db[genre_name] = {}

        for decade in genre.findall('decade'):
            decade_years = decade.get('years')
            movie_db[genre_name][decade_years] = []

            for movie in decade.findall('movie'):
                movie_info = {
                    "title": movie.get("title"),
                    "favorite": movie.get("favorite"),
                    "format": movie.find("format").text.strip(),
                    "year": movie.find("year").text.strip(),
                    "rating": movie.find("rating").text.strip(),
                    "description": movie.find("description").text.strip()
                }
                movie_db[genre_name][decade_years].append(movie_info)

    return movie_db


# Load XML on startup
movie_dict = xml_to_dict("movie.xml")


# ---------------- View Movies ----------------

def view_movies():
    for genre, decades in movie_dict.items():
        print(f"\nGenre: {genre}")
        for decade, movies in decades.items():
            print(f"  Decade: {decade}")
            for m in movies:
                print(f"    - {m['title']} ({m['year']})")


# ---------------- Add Movie ----------------

def add_movie():
    genre = input("Enter genre: ")
    decade = input("Enter decade (e.g., 1980s): ")

    title = input("Title: ")
    favorite = input("Favorite (yes/no): ")
    format_ = input("Format (DVD/Streaming/etc): ")
    year = input("Year: ")
    rating = input("Rating: ")
    description = input("Description: ")

    movie_info = {
        "title": title,
        "favorite": favorite,
        "format": format_,
        "year": year,
        "rating": rating,
        "description": description
    }

    if genre not in movie_dict:
        movie_dict[genre] = {}

    if decade not in movie_dict[genre]:
        movie_dict[genre][decade] = []

    movie_dict[genre][decade].append(movie_info)
    print("Movie added successfully!")


# ---------------- Search Movies ----------------

def search_movies():
    keyword = input("Enter keyword to search: ").lower()

    found = False
    for genre, decades in movie_dict.items():
        for decade, movies in decades.items():
            for m in movies:
                if keyword in m["title"].lower() or keyword in m["description"].lower():
                    print(f"\nFound in {genre} - {decade}:")
                    print(f"  {m['title']} ({m['year']})")
                    found = True

    if not found:
        print("No matching movies found.")


# ---------------- Delete Movie ----------------

def delete_movie():
    title = input("Enter the title of the movie to delete: ").lower()

    for genre, decades in movie_dict.items():
        for decade, movies in decades.items():
            for m in movies:
                if m["title"].lower() == title:
                    movies.remove(m)
                    print("Movie deleted.")
                    return

    print("Movie not found.")


# ---------------- Edit Movie ----------------

def edit_movie():
    title = input("Enter the title of the movie to edit: ").lower()

    for genre, decades in movie_dict.items():
        for decade, movies in decades.items():
            for m in movies:
                if m["title"].lower() == title:
                    print("Leave blank to keep existing value.")

                    new_title = input(f"New title ({m['title']}): ") or m["title"]
                    new_fav = input(f"Favorite ({m['favorite']}): ") or m["favorite"]
                    new_format = input(f"Format ({m['format']}): ") or m["format"]
                    new_year = input(f"Year ({m['year']}): ") or m["year"]
                    new_rating = input(f"Rating ({m['rating']}): ") or m["rating"]
                    new_desc = input(f"Description ({m['description']}): ") or m["description"]

                    m.update({
                        "title": new_title,
                        "favorite": new_fav,
                        "format": new_format,
                        "year": new_year,
                        "rating": new_rating,
                        "description": new_desc
                    })

                    print("Movie updated.")
                    return

    print("Movie not found.")


# ---------------- Save / Load ----------------

def save_database():
    with open("movies.json", "w") as f:
        json.dump(movie_dict, f, indent=4)
    print("Database saved to movies.json")


def load_database():
    global movie_dict
    with open("movies.json") as f:
        movie_dict = json.load(f)
    print("Database loaded from movies.json")


# ---------------- Menu ----------------

def menu():
    while True:
        print("\n--- Movie Database Menu ---")
        print("1. View all movies")
        print("2. Add a movie")
        print("3. Edit a movie")
        print("4. Delete a movie")
        print("5. Search movies")
        print("6. Save database")
        print("7. Load database")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            edit_movie()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            search_movies()
        elif choice == "6":
            save_database()
        elif choice == "7":
            load_database()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the menu
menu()

