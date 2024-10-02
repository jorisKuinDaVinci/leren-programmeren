def vraag():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    woonplaats = input("Wat is je woonplaats? ")
    return {"naam": naam, "leeftijd": leeftijd, "woonplaats": woonplaats}

def verzamel():
    lijst = []
    antwoord = ""
    while antwoord != "stop":
        lijst.append(vraag())
        antwoord = input("Toets enter om door te gaan of stop om te printen: ")
    return lijst