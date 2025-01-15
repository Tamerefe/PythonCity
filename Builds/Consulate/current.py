import pycountry

def getcurrent(countryname):

    try:
        country = pycountry.countries.lookup(countryname)
        
        current = pycountry.currencies.get(numeric=country.numeric)

        return f"{country.name} uses the {current.name} currency."
    except LookupError:
        return "Country not found."

countryname = input("Enter a country name: ")
print(getcurrent(countryname))