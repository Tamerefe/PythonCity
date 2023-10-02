dicti = {
    "name" : "Faik",
    "age"  : "32",
    "location"    : "Berlin",
    "bornCountry" : "Istanbul"
}

print(dicti)

dictic = {
    "name" : "Faik",
    "age"  : "32",
    "location"    : {
        "bornCountry" : "Istanbul",
        "liveCountry" : "Berlin"
    }
    
}
print(dictic)

print(dicti["age"])
print(dictic["location"])
print(dictic["location"]["liveCountry"])
print(dictic.get("location").get("liveCountry"))
print(dictic.keys())

