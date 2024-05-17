from random import shuffle

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

lootjes = namen.copy()


while True:
    fout = False
    shuffle(lootjes)
    for i in range(len(namen)):
        if namen[i] == lootjes[i]:
            shuffle(lootjes)
            fout = True
            break
    if not fout:
        break