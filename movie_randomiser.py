# Program to randomise movie choice originating from randomised genre
# Author: Stephen C
# Date: 29/01/26
import random

def print_dictionary():

    genres = {1: 'Action/Adventure & Epic', 2: 'Comedy', 3: 'Drama',
                  4: 'Horror', 5: 'Musical', 6: 'Romance',
                  7: 'Science Fiction & Fantasy', 8: 'Mystery & Thriller',
                  9: 'War', 10: 'Western'}

    # user_input = input("Would you like to see a list of genres?: ")
    # if user_input == 'y' or user_input == 'Y':
    #     print("Genres:")
    #     for item in genres.values():
    #         print("{}".format(item))

    movies = {1: 'Napoléon', 2: 'Cleopatra', 3: 'The Adventures Of Robin Hood',
        4: 'Gone With The Wind', 5: 'The Sea Hawk', 6: 'The Treasure of the Sierra Madre',
        7: 'The Wages of Fear (Le Salaire de la peur)', 8: 'The Seven Samurai (Shichinin no samurai)',
        9: 'The Ten Commandments', 10: 'War and Peace', 11: 'The Vikings', 12: 'North by Northwest',
        13: 'Ben-Hur', 14: 'Spartacus', 15: 'Lawrence of Arabia', 16: 'Zulu',
        17: 'Dr Zhivago', 18: 'The Charge of the Light Brigade', 19: 'The Lion in Winter',
        20: 'Waterloo', 21: 'Aguirre: The Wrath of God (Aguirre, der Zorn Gottes',
        22: 'The Poseidon Adventure', 23: 'Enter the Dragon', 24: 'Papillon',
        25: 'The Towering Inferno', 26: 'Raiders of the Lost Ark', 27: 'Fitzcarraldo',
        28: 'Gandhi', 29: 'The Right Stuff', 30: 'A Passage To India', 31: 'Ran',
        32: 'The Mission', 33: 'Top Gun', 34: 'The Last Emperor', 35: 'Die Hard'}
    movies_2 = {1: 'Safety Last', 2: 'The General', 3: 'Duck Soup', 4: 'It\'s A Gift',
        5: 'Modern Times', 6: 'Nothing Sacred', 7: 'Way Out West',
        8: 'Bringing Up Baby', 9: 'His Girl Friday', 10: 'Sullivan\'s Travel'}
    movies_3 = {1: 'Mr Smith Goes To Washington', 2: 'The Grapes of Wrath',
        3: 'Citizen Kane', 4: 'The Lost Weekend',
        5: 'The Best Years of Our Lives', 6: 'Great Expectations',
        7: 'It\'s a Wonderful Life', 8: 'The Bicycle Thief (Ladri di Biciclette)',
        9: 'All About Eve', 10: 'Sunset Boulevard'}
    movies_4 = {1: 'Nosferatu', 2: 'The Phantom of the Opera', 3: 'Freaks',
        4: 'King Kong', 5: 'Bride of Frankenstein', 6: 'Dead of Night',
        7: 'Les Diaboliques', 8: 'Dracula', 9: 'Psycho', 10: 'Peeping Tom'}
    movies_5 = {1: '42nd Street', 2: 'Gold Diggers of 1933', 3: 'The Gay Divoercee',
        4: 'Top Hat', 5: 'Show Boat', 6: 'Alexander\'s Ragtime Band',
        7: 'The Wizard of Oz', 8: 'Yankee Doodle Dandy',
        9: 'The Gang\'s All Here', 10: 'Meet Me in St. Louis'}
    movies_6 = {1: 'Sunrise', 2: 'It Happened One Night', 3: 'Camille',
        4: 'Wuthering Heights', 5: 'The Shop Around The Corner',
        6: 'Waterloo Bridge', 7: 'The Philadelphia Story',
        8: 'The Lady Eve', 9: 'Casablanca', 10: 'Now, Voyager'}
    movies_7 = {1: 'Metropolis', 2:'Lost Horizon',
        3: 'The Day The Earth Stood Still', 4: 'War of the Worlds',
        5: 'Forbidden Planet', 6: 'Invasion of the Body Snatchers',
        7: 'Jason and the Argonauts',
        8: 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb',
        9: 'Planet of the Apes', 10: '2001: A Space Odyssey'}
    movies_8 = {1: 'Little Caesar', 2: 'The Public Enemy', 3: 'Rebecca',
        4: 'The Maltese Falcon', 5: 'Double Indemnity', 6: 'The Big Sleep',
        7: 'Kiss of Death', 8: 'The Third Man', 9: 'Strangers on a Train',
        10: 'The Big Heat'}
    movies_9 = {1: 'Wings', 2: 'All Quiet on the Western Front',
        3: 'La Grande Illusion (The Grand Illusion)', 4: 'In Which We Serve',
        5: 'Five Graves To Cairo', 6: 'The Life and Death of Colonel Blimp',
        7: 'Rome, Open City (Roma, citta aperta)', 8: 'They Were Expendable',
        9: 'Battle Ground', 10: 'Sands of Iwo Jima'}
    movies_10 = {1: 'Union Pacific', 2: 'Stagecoach',
        3: 'The Ox-Bow Incident', 4: 'Duel in the Sun', 5: 'My Darling Clementine',
        6: 'Fort Apache', 7: 'Red River', 8: 'She Wore a Yellow Ribbon',
        9: 'The Gunfighter', 10: 'Winchester \'73'
        }

    choice = input('Would you like to see a list of genres or movies?: ')
    if choice == 'Yes' or choice == 'Y':
        user_input = input("Would you like to see a list of genres?: ")
        if user_input == 'y' or user_input == 'Y':
            print("Genres:")
            for item in genres.values():
                print("{}".format(item))
            # Come back to below. If 'n' to genre, give user a choice for movies
            # genre_movie = input('\nWould you like to see a list of movies too?: ')
            # if genre_movie == 'y' or genre_movie == 'Y':
        elif user_input == 'n' or user_input == 'N':
            movie_input = input("\nWhat about a list of movies?: ")
            if movie_input == 'y' or movie_input == 'Y':
                user_choice = input('What genre of movie would you like to see?: ')
                if user_choice == 'Action' or user_choice == 'Adventure' or user_choice == 'Epic':
                    print("Action/Adventure and Epic movies:")
                    for item in movies.values():
                        print(item)
                elif user_choice == 'Comedy':
                    print("Comedy movies:")
                    for item in movies_2.values():
                        print("{}".format(item))
                elif user_choice == 'Drama':
                    print("Drama movies:")
                    for item in movies_3.values():
                        print("{}".format(item))
                elif user_choice == 'Horror':
                    print("Horror movies:")
                    for item in movies_4.values():
                        print("{}".format(item))
                elif user_choice == 'Musical':
                    print("Musical movies:")
                    for item in movies_5.values():
                        print("{}".format(item))
                elif user_choice == 'Romance':
                    print("Romance movies:")
                    for item in movies_6.values():
                        print("{}".format(item))
                elif user_choice == 'Science Fiction & Fantasy' or user_choice == 'Sci-Fi' or user_choice == 'Fantasy':
                    print("Science Fiction & Fantasy movies:")
                    for item in movies_7.values():
                        print("{}".format(item))
                elif user_choice == 'Mystery & Thriller' or user_choice == 'Mystery' or user_choice == 'Thriller':
                    print("Mystery & Thriller movies:")
                    for item in movies_8.values():
                        print("{}".format(item))
                elif user_choice == 'War':
                    print("War movies:")
                    for item in movies_9.values():
                        print("{}".format(item))
                elif user_choice == 'Western':
                    print("Western movies:")
                    for item in movies_10.values():
                        print("{}".format(item))
            elif user_input == 'No' or user_input == 'N':
                print('Okay! We\'ll choose a movie for you to watch instead.')

    elif choice == 'No' or choice == 'N':
        print('Okay! We\'ll choose a movie for you to watch instead.')

    return genres, movies, movies_2, movies_3, movies_4, movies_5, movies_6, movies_7, movies_8, movies_9, movies_10


def genre(genres):
    genre_choice = random.choice(list(genres.values()))
    print('\nI\'ve randomised a genre from the list, it\'s shown below.')
    print('Genre: ', genre_choice)

    return genre_choice

def movie_choice(genre_choice):

    if genre_choice == 'Action/Adventure & Epic':
        movie = random.choice(list(movies.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Comedy':
        movie = random.choice(list(movies_2.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Drama':
        movie = random.choice(list(movies_3.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Horror':
        movie = random.choice(list(movies_4.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Musical':
        movie = random.choice(list(movies_5.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Romance':
        movie = random.choice(list(movies_6.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Science Fiction & Fantasy':
        movie = random.choice(list(movies_7.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Mystery & Thriller':
        movie = random.choice(list(movies_8.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'War':
        movie = random.choice(list(movies_9.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)
    elif genre_choice == 'Western':
        movie = random.choice(list(movies_10.values()))
        print(f'\nThe {genre_choice.lower()} movie you should watch is shown below.')
        print('Movie: ', movie)

    return movie


def seen_movies(movie):
    seen_movies = {}
    choice = input('\nHave you seen this movie? (\'Yes or No\'): ')
    if choice == 'Yes' or choice == 'Y':
        seen_movies[movie] = 1
    else:
        print('Enjoy the film!')

    for item in seen_movies.keys():
        print("{}".format(item))
    # print(seen_movies.keys())


def main(genre_choice):

    movie = movie_choice(genre_choice)
    return movie

if __name__ == '__main__':
    genre_choice, movies, movies_2, movies_3, movies_4, movies_5, movies_6, movies_7, movies_8, movies_9, movies_10 = print_dictionary()
    genre_choice = genre(genre_choice)
    movie = main(genre_choice)
    seen_movies(movie)