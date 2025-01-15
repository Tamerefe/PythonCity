from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError

geo = Nominatim(user_agent="myGeocoder")

place = input("Enter the name of the place: ")

location = geo.geocode(place)
if location:
    print(location)
else:
    print("Location not found")