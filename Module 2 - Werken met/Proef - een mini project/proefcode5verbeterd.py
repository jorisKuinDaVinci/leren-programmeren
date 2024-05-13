#Vraag namen op van deelnemers (alle namen moeten uniek zijn)
#Bij minder dan 3 namen, blijf je doorvragen naar namen.
#Als er 3 namen ingevoerd zijn dan krijgt de gebruiker de optie om nog een naam in te voeren of kunnen er lootjes worden getrokken
#Iedereen krijgt (random) één uniek lootje
#Aan het einde mag niemand het lootje van zichzelf hebben
#Als alles verdeeld is wordt er een lijst met namen geprint en de bijbehorende lootjes
from random import shuffle, choice

def geef_naam(namen):
    while True:
        naam = input("Geef een naam: ").lower()
        if naam in namen:
            print("Deze naam is al ingevoerd, probeer een andere naam.")
        else:
            return naam

namen = []

while True:
    naam = geef_naam(namen)
    namen.append(naam)
    if len(namen) >= 3 and input("Wil je nog een naam invoeren? ").lower() != "ja":
        break

shuffle(namen)

lootjes = namen.copy()
shuffle(lootjes)


while True:
    fout = False
    for i in range(len(namen)):
        if namen[i] == lootjes[i]:
            shuffle(lootjes)
            fout = True
            break
    if not fout:
        break

for i in range(len(namen)):
    print(f"{namen[i]} heeft het lootje van {lootjes[i]}")