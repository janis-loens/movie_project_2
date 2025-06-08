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
    with open("movie_database.json", "r") as file:
        content = json.loads(file.read())
    return content


def save_movies(movies) -> None:
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    json_string = json.dumps(movies)
    with open("movie_database.json", "w") as file:
        file.write(json_string)


def add_movie(title, year, rating) -> None:
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("movie_database.json", "r") as file:
        content = json.loads(file.read())
    content.append({"title": title,
                    "year": year,
                    "rating": rating})

    json_string = json.dumps(content)

    with open("movie_database.json", "w") as file:
        file.write(json_string)


def delete_movie(title) -> None:
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("movie_database.json", "r") as file:
        content = json.loads(file.read())
    for movie in content:
        if movie["title"] == title:
            content.remove(movie)

    json_string = json.dumps(content)

    with open("movie_database.json", "w") as file:
        file.write(json_string)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("movie_database.json", "r") as file:
        content = json.loads(file.read())
    for movie in content:
        if movie["title"] == title:
            movie["rating"] = rating

    json_string = json.dumps(content)

    with open("movie_database.json", "w") as file:
        file.write(json_string)
