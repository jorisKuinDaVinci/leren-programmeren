from random import shuffle

def geef_naam(namen):
    #Vraagt de gebruiker een naam in te voeren en controleert of deze al bestaat.
    #Retourneert een unieke naam.
    #.strip() verwijdert spaties aan het begin en einde van de string.
    while True:
        naam = input("Geef een naam: ").strip()
        if naam.lower() in [n.lower() for n in namen]:
            print("Deze naam is al ingevoerd, probeer een andere naam.")
        else:
            return naam

def vraag_cadeautjes(naam):
    #Vraagt drie cadeautjes voor een specifieke naam.
    #Retourneert een lijst met cadeautjes.
    #.strip() verwijdert spaties aan het begin en einde van de string.
    cadeautjes = []
    print(f"Vul drie cadeautjes in voor {naam}.")
    for i in range(1, 4):
        cadeau = input(f"Cadeau {i}: ").strip()
        cadeautjes.append(cadeau)
    return cadeautjes

# Verzamel namen en cadeautjes
namen = []
cadeautjes_per_persoon = {}

while True:
    naam = geef_naam(namen)
    namen.append(naam)
    cadeautjes_per_persoon[naam] = vraag_cadeautjes(naam)
    if len(namen) >= 3 and input("Wil je nog een naam invoeren? (ja/nee) ").lower() != "ja":
        break

# Lootjes trekken
lootjes = namen.copy()

while True:
    fout = False
    shuffle(lootjes)
    for i in range(len(namen)):
        if namen[i] == lootjes[i]:
            fout = True
            break
    if not fout:
        break

# Resultaat weergeven
print("\nDe lootjes en cadeautjes zijn als volgt verdeeld:")
for i in range(len(namen)):
    getrokken = lootjes[i]
    print(f"{namen[i]} heeft {getrokken} getrokken.")
    print(f"Cadeautjeslijst voor {getrokken}: {', '.join(cadeautjes_per_persoon[getrokken])}")
    print("-" * 40)