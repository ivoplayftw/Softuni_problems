class Movie:
    def __init__(self, name: str, director: str, watched = False,):
        self.name = name
        self.director = director
        self.watched = watched
        self.__watched_movies = 0
        
    def change_name(self, name: str):
        self.name = name
        
    def change_director(self, director: str):
        self.director = director
        
    def watch(self):
        if self.watched == False:
            self.__watched_movies += 1
            self.watched = True
    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {self.__watched_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)