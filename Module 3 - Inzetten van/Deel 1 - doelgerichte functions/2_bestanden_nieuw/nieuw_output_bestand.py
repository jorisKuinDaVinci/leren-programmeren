from functie_bestand import *

functie = verzamel()

for i in functie:
    print(f"in {i['woonplaats']} woont de {i['leeftijd']} jarige {i['naam']}")