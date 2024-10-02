def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    return {"naam": naam, "leeftijd": leeftijd}

functie = vraag_naam_en_leeftijd()
print(f"{functie['naam']} is {functie['leeftijd']} jaar")