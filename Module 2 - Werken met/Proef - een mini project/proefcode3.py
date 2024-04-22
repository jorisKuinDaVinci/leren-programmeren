from random import shuffle, choice

def geef_naam(namen_set):
    while True:
        naam = input("Geef een naam: ")
        if naam in namen_set:
            print("Deze naam is al ingevoerd, probeer een andere naam.")
        else:
            namen_set.add(naam)
            return naam

namen_set = set()
namen = []
while len(namen) < 3:
    naam = geef_naam(namen_set)
    namen.append(naam)

wil_je_nog_een_naam = input("Wil je nog een naam invoeren? ")
while wil_je_nog_een_naam == "ja":
    naam = geef_naam(namen_set)
    namen.append(naam)
    wil_je_nog_een_naam = input("Wil je nog een naam invoeren? ")

shuffle(namen)

#Iedereen krijgt (random) één uniek lootje.
#Aan het einde mag niemand het lootje van zichzelf hebben.
#aan het einde mag niemand twee keer gekozen zijn.
#Als alles verdeeld is wordt er een lijst met namen geprint en de bijbehorende lootjes.

def lootjes_trekken(namen):
    lootjes = []
    for i in range(len(namen)):
        lootje = namen[i]
        while lootje == namen[i]:
            lootje = choice(namen)
        lootjes.append(lootje)
    return lootjes

lootjes = lootjes_trekken(namen)

for i in range(len(namen)):
    print(f"{namen[i]} heeft het lootje van {lootjes[i]}")