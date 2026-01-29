# Program to randomise movie choice originating from randomised genre
# Author: Stephen C
# Date: 29/01/26
import random

def genre():
    genres = {1: 'Action/Adventure & Epic', 2: 'Comedy', 3: 'Drama',
              4: 'Horror', 5: 'Musical', 6: 'Romance',
              7: 'Science Fiction & Fantasy', 8: 'Mystery & Thriller',
              9: 'War', 10: 'Western'}
    genre_choice = random.choice(list(genres.values()))
    print(genre_choice)
    return genre_choice

def movie(genre_choice):
    movies = {1: 'Napoléon', 2: 'Cleopatra', 3: 'The Adventures Of Robin Hood'}
    movies_2 = {1: 'Safety Last', 2: 'The General', 3: 'Duck Soup'}
    if genre_choice == 'Action/Adventure & Epic':
        movie = random.choice(list(movies.values()))
        print(movie)
    elif genre_choice == 'Comedy':
        movie = random.choice(list(movies_2.values()))
        print(movie)

    # return movie

def main():

    selected_genre = genre()
    movie(selected_genre)

if __name__ == '__main__':
    main()