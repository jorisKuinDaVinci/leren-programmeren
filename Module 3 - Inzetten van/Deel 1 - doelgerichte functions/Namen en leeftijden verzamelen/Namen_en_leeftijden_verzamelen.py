def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    return {"naam": naam, "leeftijd": leeftijd}

def verzamel_naam_en_leeftijd():
    lijst = []
    vraag = ""
    while vraag != "stop":
        lijst.append(vraag_naam_en_leeftijd())
        vraag = input("Toets enter om door te gaan of stop om te printen: ")
    return lijst

functie = verzamel_naam_en_leeftijd()
for i in functie:
    print(f"{i['naam']} is {i['leeftijd']} jaar")