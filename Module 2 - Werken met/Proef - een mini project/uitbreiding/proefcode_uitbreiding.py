from proefcode_code import *
#Een lijstje tonen zodat iedereen kan zie wie wie heeft is natuurlijk niet heel handig, maak daarom de volgende uitbreiding:

#Je programma houdt nu de uitslag geheim en wie wie heeft kan opgevraagd worden door 1 van de namen uit de namenlijst in te vullen. 
#Dan geeft het programma de naam terug waar het lootje aan gekoppeld is.


while True:
    naam = input("Van wie wil je weten wie hij/zij heeft? ").lower()
    if naam in namen:
        print(f"{naam} heeft {lootjes[namen.index(naam)]}")
    else:
        print("Deze naam is niet bekend.")
    if input("Wil je nog een naam opvragen? ").lower() != "ja":
        break