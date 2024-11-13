import webbrowser

def open_map(location):
    webbrowser.open('https://www.google.com/maps/place/' + location)


city = input('Enter a city: ')
open_map(city)