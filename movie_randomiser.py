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
    print('Genre: ', genre_choice)
    return genre_choice

def movie(genre_choice):
    movies = {1: 'Napoléon', 2: 'Cleopatra', 3: 'The Adventures Of Robin Hood',
    4: 'Gone With The Wind', 5: 'The Sea Hawk', 6: 'The Treasure of the Sierra Madre',
    7: 'The Wages of Fear (Le Salaire de la peur)', 8: 'The Seven Samurai (Shichinin no samurai)',
    9: 'The Ten Commandments', 10: 'War and Peace'}
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
    8: ' The Lady Eve', 9: 'Casablanca', 10: 'Now, Voyager'}
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
    if genre_choice == 'Action/Adventure & Epic':
        movie = random.choice(list(movies.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Comedy':
        movie = random.choice(list(movies_2.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Drama':
        movie = random.choice(list(movies_3.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Horror':
        movie = random.choice(list(movies_4.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Musical':
        movie = random.choice(list(movies_5.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Romance':
        movie = random.choice(list(movies_6.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Science Fiction & Fantasy':
        movie = random.choice(list(movies_7.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Mystery & Thriller':
        movie = random.choice(list(movies_8.values()))
        print('Movie: ', movie)
    elif genre_choice == 'War':
        movie = random.choice(list(movies_9.values()))
        print('Movie: ', movie)
    elif genre_choice == 'Western':
        movie = random.choice(list(movies_10.values()))
        print('Movie: ', movie)

    # return movie

def main():

    selected_genre = genre()
    movie(selected_genre)

if __name__ == '__main__':
    main()