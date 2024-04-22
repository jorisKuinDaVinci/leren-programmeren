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

lootjes = namen.copy()
shuffle(lootjes)


if lootjes[-1] == namen[-1]:
    index = choice(range(len(namen) - 1))
    lootjes[-1], lootjes[index] = lootjes[index], lootjes[-1]

for i in range(len(namen)):
    print(f"{namen[i]} heeft het lootje van {lootjes[i]}")