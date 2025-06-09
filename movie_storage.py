import json


def get_movies() -> list:
    """
    Returns a list of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data. 

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    try:
        with open("movie_database.json", "r", encoding="utf-8") as file:
            content = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        raise RuntimeError("Could not parse movie_database.json") from e

    if not isinstance(content, list):
        raise RuntimeError("movie_database.json is malformed: expected a list of movies")

    for entry in content:
        if not all(k in entry for k in ("title", "year", "rating")):
            raise RuntimeError(f"Malformed entry in database: {entry!r}")
    return content


def save_movies(movies) -> None:
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    try:
        with open("movie_database.json", "w", encoding="utf-8") as f:
            json.dump(movies, f, indent=2)
    except OSError as e:
        raise RuntimeError("Failed to write movie_database.json") from e


def add_movie(title, year, rating) -> None:
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    content = get_movies()

    content.append({"title": title,
                    "year": year,
                    "rating": rating})

    save_movies(content)


def delete_movie(title) -> None:
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    content = get_movies()

    for movie in content:
        if movie["title"] == title:
            content.remove(movie)

    save_movies(content)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    content = get_movies()

    for movie in content:
        if movie["title"] == title:
            movie["rating"] = rating

    save_movies(content)

