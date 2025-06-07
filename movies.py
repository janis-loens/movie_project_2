from statistics import median as get_median
import matplotlib.pyplot as plt
import random

movies = {
    "The Shawshank Redemption": 9.5,
    "Pulp Fiction": 8.8,
    "The Room": 3.6,
    "The Godfather": 9.2,
    "The Godfather: Part II": 9.0,
    "The Dark Knight": 9.0,
    "12 Angry Men": 8.9,
    "Everything Everywhere All At Once": 8.9,
    "Forrest Gump": 8.8,
    "Star Wars: Episode V": 8.7
}


def pause() -> None:
    """
    Pauses program execution to give the user time to read the output.

    Returns:
        None
    """

    input("\nPress Enter to continue.")


def ensure_not_empty(dict_of_movies: dict) -> None:
    """
    Ensures a dictionary is not empty.
    Args:
        dict_of_movies (dict): A dictionary

    Returns:
        None

    Raises:
        ValueError: If the dictionary is empty.
    """

    if not dict_of_movies:
        raise ValueError("Dictionary is empty.")


def get_valid_rating() -> float:
    """
    Ensures the given rating is float between 0 and 10 included.

    Returns:
        float: A float between 0 and 10.
    """
    while True:
        try:
            rating = float(input("Enter a movie rating (0–10): "))
            if not (0 <= rating <= 10):
                raise ValueError
            return rating
        except ValueError:
            print("Invalid rating. Please enter a number between 0 and 10.")


def list_movies(dict_of_movies: dict) -> None:
    """
    Prints the total number of movies and their ratings from a given dictionary.

    Args:
        dict_of_movies (dict): A dictionary with movie names as keys and their ratings as values.

    Returns:
        None
    """

    print(f"The Database contains a total of {len(dict_of_movies)} movies.\n")
    for movie_name, rating in dict_of_movies.items():
        print(f"{movie_name}: {rating}")


def add_movie(movie_name: str, movie_rating: float) -> None:
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

    if movie_name in movies:
        raise ValueError(f"Movie '{movie_name}' already exists.")
    movies[movie_name] = movie_rating


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

    if movie_name not in movies:
        raise KeyError(f"Movie '{movie_name}' does not exist.")
    del movies[movie_name]


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

    if movie_name not in movies:
        raise KeyError(f"Movie '{movie_name}' does not exist.")
    movies[movie_name] = new_movie_rating


def movies_stats(dictionary_of_movies: dict) -> tuple:
    """
    Return statistical information about the movie dictionary: average rating, median rating, best and worst movies.

    Args:
        dictionary_of_movies (dict): A dictionary with movie titles as keys and ratings (0–10) as values.

    Returns:
        tuple:
            average_rating (float): The average of all movie ratings.
            best_movie (tuple): A tuple of the highest-rated movie (name, rating).
            worst_movie (tuple): A tuple of the lowest-rated movie (name, rating).
            median_rating (float): The median of all movie ratings.

    Raises:
        ValueError: If the dictionary is empty.
    """

    ensure_not_empty(dictionary_of_movies)

    ratings = list(dictionary_of_movies.values())
    sum_of_ratings = sum(ratings)

    best_movie = max(dictionary_of_movies.items(), key=lambda x: x[1])
    worst_movie = min(dictionary_of_movies.items(), key=lambda x: x[1])
    average_rating = sum_of_ratings / len(ratings)
    median_rating = get_median(ratings)

    return average_rating, best_movie, worst_movie, median_rating


def get_random_movie(dict_of_movies: dict) -> tuple:
    """
    Return a random movie and its rating from the dictionary.

    Args:
        dict_of_movies (dict): A dictionary with movie names as keys and ratings as values.

    Returns:
        tuple: A randomly selected (movie name, rating) pair.

    Raises:
        ValueError: If the dictionary is empty.
    """

    ensure_not_empty(dict_of_movies)

    random_movie = random.choice(list(dict_of_movies.items()))
    return random_movie

def search_movie(dict_of_movies: dict, part_of_movie_name: str) -> list:
    """
    Return all movies containing the input string, case-insensitive.

    Args:
        dict_of_movies (dict): A dictionary with movie names as keys and ratings as values.
        part_of_movie_name (str): A substring to search for within movie titles.

    Returns:
        list of tuple: A list of (movie name, rating) pairs that match the search.

    Raises:
        ValueError: If the dictionary is empty.
        KeyError: If no movies match the search string.
    """

    ensure_not_empty(dict_of_movies)

    list_of_movie_tuples = []
    for movie_name, movie_rating in dict_of_movies.items():
        if part_of_movie_name.lower() in movie_name.lower():
            list_of_movie_tuples.append((movie_name, movie_rating))
    if len(list_of_movie_tuples) == 0:
        raise KeyError(f"Movie with '{part_of_movie_name}' in it could not be found.")
    return list_of_movie_tuples


def sort_movies_by_rating(dict_of_movies: dict) -> list:
    """
    Sort movies by rating in descending order.

    Args:
        dict_of_movies (dict): A dictionary with movie names as keys and ratings as values.

    Returns:
        list of tuple: A list of (movie name, rating) pairs sorted by rating in descending order.

    Raises:
        ValueError: If the dictionary is empty.
    """

    ensure_not_empty(dict_of_movies)

    sorted_movie_list = sorted(dict_of_movies.items(), key=lambda x: x[1], reverse=True)
    return sorted_movie_list

def create_histogram(dict_of_movies):
    ratings_list = []
    for rating in dict_of_movies.values():
        ratings_list.append(rating)
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
    
        Enter choice (1-10):
        
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
                add_movie(input_movie_name, input_rating)
                print(f"Movie '{input_movie_name}' successfully added.")

            except ValueError as ve:
                print(f"Error: {ve}")

            finally:
                pause()

        elif user_choice == "3":
            input_movie_name = input("Enter a movie name to delete: ")

            try:
                delete_movie(input_movie_name)
                print(f"Movie '{input_movie_name}' successfully deleted.")

            except KeyError as ke:
                print(f"Error: {ke}")

            finally:
                pause()

        elif user_choice == "4":
            input_movie_name = input("Enter a movie name to update: ")

            try:
                if input_movie_name not in movies:
                    raise KeyError(f"Movie '{input_movie_name}' does not exist.")

                input_new_rating = get_valid_rating()
                update_movie(input_movie_name, input_new_rating)
                print(f"Movie '{input_movie_name}' successfully updated.")

            except KeyError as ke:
                print(f"Error: {ke}")

            except ValueError as ve:
                print(f"Error: {ve}")

            finally:
                pause()


        elif user_choice == "5":
            try:
                average_rating, best_movie, worst_movie, median_rating = movies_stats(movies)
                print(f"Average rating: {average_rating}")
                print(f"Median rating: {median_rating}")
                print(f"Best movie: {best_movie[0]}, {best_movie[1]}")
                print(f"Worst movie: {worst_movie[0]}, {worst_movie[1]}")

            except ValueError as ve:
                print(f"Error: {ve}")

            finally:
                pause()

        elif user_choice == "6":
            try:
                movie_name, movie_rating = get_random_movie(movies)
                print(f"Your movie for tonight: {movie_name}, it's rated {movie_rating}.")

            except ValueError as ve:
                print(f"Error: {ve}")

            finally:
                pause()

        elif user_choice == "7":
            try:
                part_of_movie_name = input("Enter a part of the movie name: ")
                list_of_movies_with_part_in_it = search_movie(movies, part_of_movie_name)
                for movie_name, movie_rating in list_of_movies_with_part_in_it:
                    print(f"{movie_name}: {movie_rating}")

            except ValueError as ve:
                print(f"Error: {ve}.")

            except KeyError as ke:
                print(f"Error: {ke}.")

            finally:
                pause()

        elif user_choice == "8":
            try:
                movies_sorted_by_rating = sort_movies_by_rating(movies)
                for movie_name, movie_rating in movies_sorted_by_rating:
                    print(f"{movie_name}: {movie_rating}")

            except ValueError as ve:
                print(f"Error: {ve}.")

            finally:
                pause()

        elif user_choice == "9":
            create_histogram(movies)
            pause()

        else:
            print("Invalid choice. Please choose a number between 1 and 9.")
            pause()


if __name__ == "__main__":
    main()
