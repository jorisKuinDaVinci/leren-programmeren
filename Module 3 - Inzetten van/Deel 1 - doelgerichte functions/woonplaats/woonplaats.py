def vraag():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    woonplaats = input("Wat is je woonplaats? ")
    return {"naam": naam, "leeftijd": leeftijd, "woonplaats": woonplaats}

def verzamel():
    lijst = []
    vraag = ""
    while vraag != "stop":
        lijst.append(vraag())
        vraag = input("Toets enter om door te gaan of stop om te printen: ")
    return lijst

functie = verzamel()
for i in functie:
    print(f"{i['naam']} is {i['leeftijd']} jaar en woont in {i['woonplaats']}")