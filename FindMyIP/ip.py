import os
import urllib.request as req
import json

while True:
    os.system("cls")
    print("1) Find My IP")
    print("2) Exit")
    choice = input("Your Choice: ")

    if choice == "1":
        url = "https://api.ipify.org?format=json"
        response = req.urlopen(url)
        data = json.loads(response.read())
        print("Your IP Address: ", data["ip"])
        input("Press Enter to Return to Main Menu!")
    elif choice == "2":
        quit()
    else:
        print("Invalid Choice")
        input("Press Enter to Return to Main Menu!")