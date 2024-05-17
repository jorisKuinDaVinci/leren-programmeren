from random import choice

namen = []
while True:
    naam = input("Geef een naam: ")
    if naam in namen:
        print("Deze naam is al ingevoerd, probeer een andere naam.")
    else:
        namen.append(naam)
    if len(namen) == 3:
        wil_je_nog_een_naam = input("Wil je nog een naam invoeren? ")
        if wil_je_nog_een_naam == "ja":
            naam = input("Geef een naam: ")
            if naam in namen:
                print("Deze naam is al ingevoerd, probeer een andere naam.")
            else:
                namen.append(naam)
        else:
            break
while len(namen) < 3:
    naam = input("Geef een naam: ")
    if naam in namen:
        print("Deze naam is al ingevoerd, probeer een andere naam.")
    else:
        namen.append(naam)
lootjes = []
while len(namen) > 0:
    lootje = choice(namen)
    lootjes.append(lootje)
    namen.remove(lootje)
for i in range(len(lootjes)):
    print(f"{namen[i]} heeft het lootje van {lootjes[i]}")


