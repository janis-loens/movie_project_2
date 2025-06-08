import random
from statistics import median as get_median
import matplotlib.pyplot as plt

movies = [
    {
        "title": "The Shawshank Redemption",
        "rating": 9.5,
        "year": 2012,
    },
    {
        "title": "Pulp Fiction",
        "rating": 8.8,
        "year": 2012,
    },
]


def pause() -> None:
    """
    Pauses program execution to give the user time to read the output.

    Returns:
        None
    """

    input("\nPress Enter to continue.")


def ensure_not_empty(list_of_dicts_of_movies: list[dict]) -> None:
    """
    Ensures a dictionary is not empty.
    Args:
        list_of_dicts_of_movies (list[dict]): A list that contains dictionaries of movies.
        This contains the keys "title", "rating" and "year".

    Returns:
        None

    Raises:
        ValueError: If the dictionary is empty.
    """

    if not list_of_dicts_of_movies:
        raise ValueError("List is empty.")


def get_valid_name() -> str:
    """
    Check if Name is in the list of movie names.
    Returns:
        str: A name if it is in the list of movie names.
    """
    movie_name = input("Enter a movie name: ")
    for movie in enumerate(movies):
        if movie["title"] == movie_name:
            return movie_name
    else:
        raise KeyError(f"Movie '{movie_name}' does not exist in the database.")


def get_valid_rating() -> float:
    """
    Ensures the given rating is float between 0 and 10 included.

    Returns:
        float: A float between 0 and 10.
    """
    while True:
        try:
            rating = float(input("Enter a movie rating (0–10): "))
            if not 0 <= rating <= 10:
                raise ValueError
            return rating
        except ValueError:
            print("Invalid rating. Please enter a number between 0 and 10.")


def list_movies(list_of_dicts_of_movies: list[dict]) -> None:
    """
    Prints the total number of movies and their ratings from a given dictionary.

    Args:
        list_of_dicts_of_movies (list[dict]): A list that contains dictionaries of movies.
        This contains the keys "title", "rating" and "year".

    Returns:
        None
    """

    print(f"The Database contains a total of {len(list_of_dicts_of_movies)} movies.\n")
    for movie in list_of_dicts_of_movies:
        for key, value in movie.items():
            print(f"{key.title()}: {value}")


def add_movie(movie_name: str, movie_rating: float, movie_year: int) -> None:
    """
    Add a movie to the movie dictionary, unless it is already in the dictionary.

    Args:
        movie_name (str): The name of the movie.
        movie_rating (float): The rating of the movie in the range of 0 to 10, 10 included.

    Returns:
        None

    Raises:
        ValueError: If movie name already exists.
    """
    for movie in movies:
        if movie_name in movie["title"]:
            raise ValueError(f"Movie '{movie_name}' already exists.")
    movies.append({"title": movie_name, "rating": movie_rating, "year": movie_year})


def delete_movie(movie_name: str) -> None:
    """
    Delete a movie and its rating from the movie dictionary, if it exists.

    Args:
        movie_name (str): The name of the movie to delete.

    Returns:
        None

    Raises:
        KeyError: If movie name does not exist.
    """
    for i, movie in enumerate(movies):
        if movie["title"] == movie_name:
            del movies[i]
            break
    else:
        raise KeyError(f"Movie '{movie_name}' does not exist in the database.")


def update_movie(movie_name: str, new_movie_rating: float) -> None:
    """
    Update the rating of a movie in the movie dictionary.

    Args:
        movie_name: The name of the movie.
        new_movie_rating: The new rating of the movie.

    Returns:
        None

    Raises:
        KeyError: If movie name does not exist.

    """

    for i, movie in enumerate(movies):
        if movie["title"] == movie_name:
            movies[i]["rating"] = new_movie_rating
            break

    else:
        raise KeyError(f"Movie '{movie_name}' does not exist in the database.")


def movies_stats(list_of_dictionary_of_movies: list[dict]) -> tuple:
    """
    Return statistical information about the movie dictionary: average rating, median rating, best and worst movies.

    Args:
        list_of_dictionary_of_movies (list[dict]) : A dictionary with movie titles as keys and ratings (0–10) as values.

    Returns:
        tuple:
            average_rating (float): The average of all movie ratings.
            best_movie (tuple): A tuple of the highest-rated movie (name, rating).
            worst_movie (tuple): A tuple of the lowest-rated movie (name, rating).
            median_rating (float): The median of all movie ratings.

    Raises:
        ValueError: If the dictionary is empty.
    """

    ensure_not_empty(list_of_dictionary_of_movies)

    ratings = list((movie["rating"] for movie in list_of_dictionary_of_movies))
    sum_of_ratings = sum(ratings)

    best_movie = max(
        ((m["title"], m["rating"]) for m in movies),
        key=lambda t: t[1]
    )
    worst_movie = min(
        ((m["title"], m["rating"]) for m in movies),
        key=lambda t: t[1]
    )
    average_rating = sum_of_ratings / len(ratings)
    median_rating = get_median(ratings)

    return average_rating, best_movie, worst_movie, median_rating


def get_random_movie(list_of_dict_of_movies: list[dict]) -> dict:
    """
    Return a random movie dict from the list of dictionaries of movies.

    Args:
        list_of_dict_of_movies (list[dict]): A dictionary with movie names as keys and ratings as values.

    Returns:
        dict: A randomly selected movie dict.

    Raises:
        ValueError: If the dictionary is empty.
    """

    ensure_not_empty(list_of_dict_of_movies)

    random_movie = random.choice(list_of_dict_of_movies)
    return random_movie


def search_movie(list_of_dict_of_movies: list[dict], part_of_movie_name: str) -> list:
    """
    Return all movies containing the input string, case-insensitive.

    Args:
        list_of_dict_of_movies (list[dict]): A dictionary with movie names as keys and ratings as values.
        part_of_movie_name (str): A substring to search for within movie titles.

    Returns:
        list of tuple: A list of (movie name, rating) pairs that match the search.

    Raises:
        ValueError: If the dictionary is empty.
        KeyError: If no movies match the search string.
    """

    ensure_not_empty(list_of_dict_of_movies)

    list_of_movie_tuples = []
    for movie in list_of_dict_of_movies:
        if part_of_movie_name.lower() in movie["title"].lower():
            list_of_movie_tuples.append((movie["title"], movie["rating"]))
    if len(list_of_movie_tuples) == 0:
        raise KeyError(f"Movie with '{part_of_movie_name}' in it could not be found.")
    return list_of_movie_tuples


def sort_movies_by_rating(list_of_dict_of_movies: list[dict]) -> list:
    """
    Sort movies by rating in descending order.

    Args:
        list_of_dict_of_movies (list[dict]): A dictionary with movie names as keys and ratings as values.

    Returns:
        list of tuple: A list of (movie name, rating) pairs sorted by rating in descending order.

    Raises:
        ValueError: If the dictionary is empty.
    """

    ensure_not_empty(list_of_dict_of_movies)

    sorted_movie_list = sorted(((m["title"], m["rating"]) for m in movies), key=lambda t: t[1], reverse=True)
    return sorted_movie_list


def sort_movies_by_year(list_of_dict_of_movies: list[dict]) -> list:
    """
    Sort movies by year in descending order.

    Args:
        list_of_dict_of_movies (list[dict]): A dictionary with movie names as keys and ratings as values.

    Returns:
        list of tuple: A list of (movie name, rating) pairs sorted by rating in descending order.

    Raises:
        ValueError: If the dictionary is empty.
    """

    ensure_not_empty(list_of_dict_of_movies)

    sorted_movie_list = sorted(((m["title"], m["year"]) for m in movies), key=lambda t: t[1], reverse=True)
    return sorted_movie_list


def filter_movies(list_of_dict_of_movies: list[dict], start_rating: float, start_year: int, end_year: int) -> list[
    dict]:
    """
    Filter movies by a minimum rating and a range of years.

    Args:
        list_of_dict_of_movies (list[dict]): A dictionary with movie names as keys and ratings as values.:
        start_rating (float): The minimum rating to filter.
        start_year (int): The minimum year to filter.
        end_year (int): The maximum year to filter.

    Returns:
        list of dict: A list of filtered movie dicts.

    """
    ensure_not_empty(list_of_dict_of_movies)

    filtered_list_of_movies = []
    for movie in list_of_dict_of_movies:
        if movie["year"] >= start_year and movie["year"] <= end_year and movie["rating"] >= start_rating:
            filtered_list_of_movies.append(movie)
    return filtered_list_of_movies


def create_histogram(list_of_dict_of_movies: list[dict]) -> None:
    ratings_list = []
    for movie in list_of_dict_of_movies:
        ratings_list.append(movie["rating"])
    plt.hist(ratings_list)
    plt.show()


def main():
    """
    Main loop for the movie database CLI. Presents options to the user
    and performs operations based on user input.
    """

    menu_text = """
        ********** My Movies Database **********

        Menu:
        0. Quit
        1. List movies
        2. Add movie
        3. Delete movie
        4. Update movie
        5. Stats
        6. Random movie
        7. Search movie
        8. Movies sorted by rating
        9. Create rating histogram
        10. Filter movies
        11. Create rating histogram

        Enter choice (0-11):

        """
    while True:
        user_choice = input(menu_text)

        if user_choice == "0":
            confirm = input("Are you sure you want to quit? (y/n): ").lower()
            if confirm == "y":
                print("Goodbye!")
                break

        elif user_choice == "1":
            list_movies(movies)
            pause()

        elif user_choice == "2":
            input_movie_name = input("Enter a movie name: ")

            try:
                input_rating = get_valid_rating()
                input_year = int(input("Enter the year the movie was released: "))
                add_movie(input_movie_name, input_rating, input_year)
                print(f"Movie '{input_movie_name}' successfully added.")

            except ValueError as v_e:
                print(f"Error: {v_e}")

            finally:
                pause()

        elif user_choice == "3":
            try:
                input_movie_name = get_valid_name()
                delete_movie(input_movie_name)
                print(f"Movie '{input_movie_name}' successfully deleted.")

            except KeyError as k_e:
                print(f"Error: {k_e}")

            finally:
                pause()

        elif user_choice == "4":
            try:
                input_movie_name = get_valid_name()
                input_new_rating = get_valid_rating()
                update_movie(input_movie_name, input_new_rating)
                print(f"Movie '{input_movie_name}' successfully updated.")

            except KeyError as k_e:
                print(f"Error: {k_e}")

            except ValueError as v_e:
                print(f"Error: {v_e}")

            finally:
                pause()


        elif user_choice == "5":
            try:
                average_rating, best_movie, worst_movie, median_rating = movies_stats(movies)
                print(f"Average rating: {average_rating}")
                print(f"Median rating: {median_rating}")
                print(f"Best movie: {best_movie[0]}, {best_movie[1]}")
                print(f"Worst movie: {worst_movie[0]}, {worst_movie[1]}")

            except ValueError as v_e:
                print(f"Error: {v_e}")

            finally:
                pause()

        elif user_choice == "6":
            try:
                random_movie = get_random_movie(movies)
                print(f"Your movie for tonight: {random_movie['title']},"
                      f" it's rated {random_movie['rating']}.")

            except ValueError as v_e:
                print(f"Error: {v_e}")

            finally:
                pause()

        elif user_choice == "7":
            try:
                part_of_movie_name = input("Enter a part of the movie name: ")
                list_of_movies_with_part_in_it = search_movie(movies, part_of_movie_name)
                for movie_name, movie_rating in list_of_movies_with_part_in_it:
                    print(f"{movie_name}: {movie_rating}")

            except ValueError as v_e:
                print(f"Error: {v_e}.")

            except KeyError as k_e:
                print(f"Error: {k_e}.")

            finally:
                pause()

        elif user_choice == "8":
            try:
                movies_sorted_by_rating = sort_movies_by_rating(movies)
                for movie_name, movie_rating in movies_sorted_by_rating:
                    print(f"{movie_name}: {movie_rating}")

            except ValueError as v_e:
                print(f"Error: {v_e}.")

            finally:
                pause()

        elif user_choice == "9":
            try:
                movies_sorted_by_year = sort_movies_by_year(movies)
                for movie_name, movie_year in movies_sorted_by_year:
                    print(f"{movie_name}: {movie_year}")

            except ValueError as v_e:
                print(f"Error: {v_e}.")

            finally:
                pause()

        elif user_choice == "10":
            minimum_rating = float(input("Enter minimum rating (leave blank for no minimum rating): "))
            start_year = int(input("Enter start year (leave blank for no start year): "))
            end_year = int(input("Enter end year (leave blank for no end year): "))
            filtered_movies = filter_movies(movies, minimum_rating, start_year, end_year)
            for movie in filtered_movies:
                print(f"{movie['title']} ({movie['year']}): {movie['rating']}")
            pause()

        elif user_choice == "11":
            create_histogram(movies)
            pause()

        else:
            print("Invalid choice. Please choose a number between 0 and 11.")
            pause()


if __name__ == "__main__":
    main()
