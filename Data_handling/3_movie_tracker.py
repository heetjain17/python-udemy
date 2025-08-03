import os 
import json

FILENAME = "movies.json"

def load_movies():
  if not os.path.exists(FILENAME):
    return[]
  with open(FILENAME, 'r', encoding='utf-8') as f:
    return json.load(f)
  
def save_movies(movies):
    with open(FILENAME, 'w', encoding='utf-8') as f:
      json.dump(movies, f, indent=2)
  
def add_movies(movies):
  title = input("Enter the movie name: ").strip().lower()
  if any(movie["title"] == title for movie in movies):
    print("Movie already exists")
    return
  genre = input("Genre: ").strip().lower()

  try: 
    rating = float(input("Enter rating(0-10): "))
    if not (0 <= rating <= 10):
      raise ValueError
  except ValueError:
    print("Please enter a valid number")
  
  movies.append({"title": title, "genre": genre, "rating": rating})

  save_movies(movies)
  print("Movie added")

def search_movies(movies):
  term = input("Enter the title or genre: ").strip().lower()

  results = [
    movie for movie in movies
    if term in movie["title"].lower() or term in movie["genre"].lower()
  ]

  if not results:
    print("No matching result")
    return
  
  print(f"Found {len(results)} result(s)")

  for movie in results: 
    print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")

def view_all_movies(movies):
  if not movies:
    print("No movies found")

  for index, movie in enumerate(movies):
    print(f"{index+1} {movie["title"]} -- {movie["genre"]} -- {movie["rating"]}") 

def main():
  movies = load_movies()

  while True:
    print("\nMy Binge List")
    print("1. Add Movie")
    print("2. View All Movie")
    print("3. Search Movie")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    match choice: 
      case "1":
        add_movies(movies)
      case "2":
        view_all_movies(movies)
      case "3":
        search_movies(movies)
      case "4":
        break
      case _:
        print("Enter a valid choice")

if __name__ == "__main__":
  main()