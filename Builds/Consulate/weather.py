import requests
from bs4 import BeautifulSoup

# Ensure record file exists
try:
    with open("record.txt", "r") as file:
        pass
except FileNotFoundError:
    with open("record.txt", "w") as file:
        pass
    print("First run! Record file created")

# Function to convert temperatures
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

city = input("Enter the city name: ")
formated_city = city.replace(" ", "+")

url = f"https://www.google.com/search?q=weather+in+{formated_city}"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
temperature = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text

# Extract numeric value and unit from the temperature string
temp_value = float(temperature[:-2])
temp_unit = temperature[-1].lower()

# Convert to Kelvin and Fahrenheit
temp_in_k = convert_temperature(temp_value, temp_unit, "k")
temp_in_f = convert_temperature(temp_value, temp_unit, "f")

print(f"The temperature in {city} is {temp_value}°{temp_unit.upper()} {temp_in_k:.2f}°K {temp_in_f:.2f}°F")