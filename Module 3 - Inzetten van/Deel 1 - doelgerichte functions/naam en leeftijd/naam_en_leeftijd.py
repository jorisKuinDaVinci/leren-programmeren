#Je gaat een programma maken die een naam en leeftijd vraagt en op het scherm print. 

#De volgende eisen worden gesteld aan de applicatie:

#De gebruiker kan de namen en leeftijden zelf invullen via een input
#Aan het einde van het programma word het resultaat netjes geprint zoals dit:

#Rudi is 41 jaar

#Voor het vragen van de naam en de leeftijd maak je een functie die dit voor je doet.
#De output/return van deze functie is een dictionairy met de properties ‘naam’ en ‘leeftijd’.
#Buiten de functie doe je de print, door eerst de functie aan te roepen.
def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    return {"naam": naam, "leeftijd": leeftijd}

functie = vraag_naam_en_leeftijd()
print(f"{functie['naam']} is {functie['leeftijd']} jaar")