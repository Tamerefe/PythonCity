import pycountry
from countryinfo import CountryInfo
from pytrends.request import TrendReq
import plotly.express as px
import pandas as pd
import requests
from bs4 import BeautifulSoup
import webbrowser
from geopy.geocoders import Nominatim

def get_current(countryname):
    try:
        country = pycountry.countries.lookup(countryname)
        current = pycountry.currencies.get(numeric=country.numeric)
        return f"{country.name} uses the {current.name} currency."
    except LookupError:
        return "Country not found."

def get_details(countryname):
    country = CountryInfo(countryname)
    details = {
        "Country": country.info().get("name"),
        "Capital": country.capital(),
        "Population": country.info().get("population"),
        "Area": country.area(),
        "Borders": country.borders(),
        "Timezones": country.timezones(),
        "Currencies": country.currencies(),
        "Languages": country.languages(),
        "Region": country.region(),
        "Subregion": country.subregion(),
        "Demonym": country.demonym(),
        "Native Name": country.native_name(),
        "Calling Codes": country.calling_codes(),
        "Lat, Long": country.latlng(),
        "Translations": country.translations(),
        "Alt Spellings": country.alt_spellings(),
        "Wikipedia": country.wiki(),
        "ISO Codes": country.iso(),
        "Internet TLD": country.tld()
    }
    return details

def find_country(countryname):
    country = CountryInfo(countryname).name()
    data = pd.DataFrame({'Country': [country], 'Values': [100]})
    fig = px.choropleth(data, locations='Country', locationmode='country names', color='Values', color_continuous_scale='Inferno', title=f'Country Map Highlighting {country}')
    fig.show()

def open_map(location):
    webbrowser.open('https://www.google.com/maps/place/' + location)

def region_search(region):
    pytrends = TrendReq()
    trending = pytrends.trending_searches(pn=region)
    return trending

def get_weather(city):
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "f":
            if to_unit == "c":
                return (value - 32) * 5/9
            elif to_unit == "k":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "c":
            if to_unit == "f":
                return value * 9/5 + 32
            elif to_unit == "k":
                return value + 273.15
        elif from_unit == "k":
            if to_unit == "f":
                return (value - 273.15) * 9/5 + 32
            elif to_unit == "c":
                return value - 273.15
        return None

    formated_city = city.replace(" ", "+")
    url = f"https://www.google.com/search?q=weather+in+{formated_city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    temperature = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    temp_value = float(temperature[:-2])
    temp_unit = temperature[-1].lower()
    temp_in_k = convert_temperature(temp_value, temp_unit, "k")
    temp_in_f = convert_temperature(temp_value, temp_unit, "f")
    return f"The temperature in {city} is {temp_value}°{temp_unit.upper()} {temp_in_k:.2f}°K {temp_in_f:.2f}°F"

def get_zip(place):
    geo = Nominatim(user_agent="myGeocoder")
    location = geo.geocode(place)
    if location:
        return location
    else:
        return "Location not found"

def plot_gdp_map():
    data = {
        "Country": [
            "United States", "China", "Japan", "Germany", "India", "United Kingdom", "France", "Brazil", "Canada", "Russia",
            "Italy", "South Korea", "Australia", "Mexico", "Spain", "Indonesia", "Netherlands", "Saudi Arabia", "Turkey", "Switzerland",
            "Taiwan", "Poland", "Sweden", "Belgium", "Argentina", "Thailand", "Nigeria", "Egypt", "Pakistan", "Philippines",
            "Malaysia", "Vietnam", "Bangladesh", "UAE", "South Africa", "Colombia", "Chile", "Iran", "Israel", "Greece",
            "Portugal", "Czech Republic", "Romania", "Hungary", "New Zealand", "Kazakhstan", "Peru", "Ukraine", "Qatar", "Algeria",
            "Morocco", "Iraq", "Kuwait", "Venezuela", "Ecuador", "Slovakia", "Sri Lanka", "Dominican Republic", "Guatemala", "Oman",
            "Bulgaria", "Croatia", "Serbia", "Lithuania", "Slovenia", "Costa Rica", "Uruguay", "Panama", "Latvia", "Estonia",
            "Paraguay", "El Salvador", "Bolivia", "Luxembourg", "Iceland", "Jordan", "Bahrain", "Tunisia", "Lebanon", "Cyprus",
            "Georgia", "Armenia", "Moldova", "Myanmar", "Mongolia", "Bosnia and Herzegovina", "Albania", "North Macedonia", "Malta", "Brunei",
            "Belarus", "Botswana", "Gabon", "Namibia", "Mauritius", "Eswatini", "Suriname", "Guyana", "Lesotho", "Bhutan"
        ],
        "GDP (in Billion USD)": [
            21433, 14343, 5082, 3846, 2875, 2827, 2716, 2055, 1736, 1699,
            2001, 1657, 1393, 1260, 1246, 1119, 912, 792, 761, 703,
            668, 595, 541, 533, 449, 445, 448, 404, 278, 376,
            365, 340, 329, 421, 351, 323, 282, 231, 387, 209,
            237, 246, 248, 171, 206, 181, 202, 153, 183, 169,
            124, 234, 138, 70, 108, 105, 84, 88, 77, 76,
            69, 68, 65, 62, 61, 60, 59, 58, 57, 56,
            55, 54, 53, 52, 51, 50, 49, 48, 47, 46,
            45, 44, 43, 42, 41, 40, 39, 38, 37, 36,
            35, 34, 33, 32, 31, 30, 29, 28, 27, 26
        ]
    }
    df = pd.DataFrame(data)
    fig = px.choropleth(df, locations="Country", locationmode="country names", color="GDP (in Billion USD)", hover_name="Country", color_continuous_scale=px.colors.sequential.Plasma, title="GDP of 100 Countries in 2024")
    fig.show()

def menu():
    print("\n\033[92m1. Get current currency\033[0m")
    print("\033[92m2. Get country details\033[0m")
    print("\033[92m3. Find country on map\033[0m")
    print("\033[92m4. Open map location\033[0m")
    print("\033[92m5. Search region trends\033[0m")
    print("\033[92m6. Get weather\033[0m")
    print("\033[92m7. Get ZIP code\033[0m")
    print("\033[92m8. Plot GDP map\033[0m")
    print("\033[91m0. Exit\033[0m\n")

    choice = input("\033[93mEnter choice: \033[0m")
    return choice

if __name__ == "__main__":
    print("\n\033[94m\tWelcome to Consulate!\033[0m")
    while True:
        choice = menu()
        if choice == "1":
            countryname = input("\033[93mEnter country name: \033[0m")
            print(get_current(countryname))
        elif choice == "2":
            countryname = input("\033[93mEnter country name: \033[0m")
            print(get_details(countryname))
        elif choice == "3":
            countryname = input("\033[93mEnter country name: \033[0m")
            find_country(countryname)
        elif choice == "4":
            location = input("\033[93mEnter location: \033[0m")
            open_map(location)
        elif choice == "5":
            region = input("\033[93mEnter region: \033[0m")
            print(region_search(region))
        elif choice == "6":
            city = input("\033[93mEnter city: \033[0m")
            print(get_weather(city))
        elif choice == "7":
            place = input("\033[93mEnter place: \033[0m")
            print(get_zip(place))
        elif choice == "8":
            plot_gdp_map()
        elif choice == "0":
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")