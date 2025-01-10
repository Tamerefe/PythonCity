import requests
from bs4 import BeautifulSoup	

city = input("Enter the city name: ")
formated_city = city.replace(" ", "+")

url = f"https://www.google.com/search?q=weather+in+{formated_city}"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
temperature = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text

print(f"The temperature in {city} is {temperature}")

try:
    with open("record.txt", "r") as file:
        pass
except FileNotFoundError:
    with open("record.txt", "w") as file:
        pass
    print("First run! Record file created")