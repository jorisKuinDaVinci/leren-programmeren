from functie_bestand import *

functie = verzamel()

for i in functie:
    print(f"{i['naam']}, die in {i['woonplaats']} woont is {i['leeftijd']} jaar oud")