from functie_bestand import *

functie = verzamel()

for i in functie:
    print(f"{i['naam']} is {i['leeftijd']} jaar en woont in {i['woonplaats']}")