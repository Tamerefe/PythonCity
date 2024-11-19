from imdb import IMDb

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