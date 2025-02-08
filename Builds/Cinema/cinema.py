import emoji
import random
from imdb import IMDb

def movielist():
    print("Current Movie List:")
    movies = {
        "The Lion King": "5🎟️  left",
        "Finding Nemo": "12🎟️  left",
        "Titanic": "3🎟️  left",
        "Jurassic Park": "7🎟️  left",
        "Star Wars": "10🎟️  left",
        "The Matrix": "8🎟️  left",
        "Frozen": "4🎟️  left",
        "Toy Story": "6🎟️  left",
        "Harry Potter": "2🎟️  left",
        "The Godfather": "9🎟️  left"
    }

    for movie, emote in movies.items():
        print(f"{movie}: {textToEmote(emote)}")
    print("🎟️  represents the number of tickets left for the movie.\n")

def textToEmote(text):
    return emoji.emojize(text)

def guess_movie_from_emojis():
    movies = {
        "The Lion King": "🦁👑",
        "Finding Nemo": "🔍🐠",
        "Titanic": "🚢💔",
        "Jurassic Park": "🦖🦕",
        "Star Wars": "⭐⚔️",
        "The Matrix": "🕶️🔫",
        "Frozen": "❄️👸",
        "Toy Story": "🤠🧸",
        "Harry Potter": "⚡🧙",
        "The Godfather": "👨‍👦🍝"
    }

    print("Guess the movie from the emojis!")
    movie, emote = random.choice(list(movies.items()))
    print(f"Emojis: {emote}")
    guess = input("Your guess: ")
    if guess.lower() == movie.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {movie}.")

def get_movie_info():
    ia = IMDb()
    moviename = input("Enter the movie name: ")
    movies = ia.search_movie(moviename)

    if movies:
        movie = movies[0]
        ia.update(movie)
        directors = movie.get('directors')
        if directors:
            print("Directors:", ", ".join(str(director) for director in directors))
            print("Genres:", ", ".join(str(genre) for genre in movie.get('genres')))
            print("Plot:", movie.get('plot')[0])
            print("Year:", movie.get('year'))
            print("Rating:", movie.get('rating'))
            print("Runtime:", movie.get('runtimes')[0], "minutes")
            print("Languages:", ", ".join(str(language) for language in movie.get('languages')))
            print("Top 250 rank:", movie.get('top 250 rank'))
            print("Production companies:", ", ".join(str(company) for company in movie.get('production companies')))
            print("IMDb URL:", ia.get_imdbURL(movie))
            print("Cast:", ", ".join(str(actor) for actor in movie.get('cast')))
    else:
        print("Movie not found")

def main_menu():
    while True:
        print("Welcome to the Movie Center!!")
        print("Choose an option:")
        print("1. Guess the movie from emojis")
        print("2. Get movie information")
        print("3. Show Current Movie List")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            guess_movie_from_emojis()
        elif choice == '2':
            get_movie_info()
        elif choice == '3':
            movielist()
        elif choice == '4':
            print("Thank you for using the Movie Center!")
            break   
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()