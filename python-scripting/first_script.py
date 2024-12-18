
def check_movie_year(movie, release_year):
    
    if release_year < 2000:
        print(f"{movie} was released before 2000.")
    else:
        print(f"{movie} was released after 2000.")
        return movie

recent_movies = []

favorite_movies = [
    {"name": "The Matrix", "year": 1999},
    {"name": "Inception", "year": 2010},
    {"name": "Toy Story", "year": 1995},
    {"name": "The Dark Knight", "year": 2008},
    {"name": "Finding Nemo", "year": 2003},
    {"name": "The Lion King", "year": 1994},
]


for movie in favorite_movies:
    result = check_movie_year(movie["name"], movie["year"])
    if result is not None:  # If a value is returned
        recent_movies.append(result)

print("\nMovies released after 2000:")
print(recent_movies)

