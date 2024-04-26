from random import shuffle, choice
wil_je_nog_een_naam = "Wil je nog een naam invoeren? "
def geef_naam(namen):
    while True:
        naam = input("Geef een naam: ")
        if naam in namen:
            print("Deze naam is al ingevoerd, probeer een andere naam.")
        else:
            return naam

#namen_set = set()
namen = []

while True:
    naam = geef_naam(namen)
    namen.append(naam)
    if len(namen) >= 3 and input("Wil je nog een naam invoeren? ") != "ja":
        break

shuffle(namen)

lootjes = namen.copy()
shuffle(lootjes)


if lootjes[-1] == namen[-1] or lootjes[-1] == namen[-2] or lootjes[-1] == namen[-3]:
    index = choice(range(len(namen) - 1))
    lootjes[-1], lootjes[index] = lootjes[index], lootjes[-1]
    lootjes[-2], lootjes[index] = lootjes[index], lootjes[-2]
    lootjes[-3], lootjes[index] = lootjes[index], lootjes[-3]

for i in range(len(namen)):
    print(f"{namen[i]} heeft het lootje van {lootjes[i]}")