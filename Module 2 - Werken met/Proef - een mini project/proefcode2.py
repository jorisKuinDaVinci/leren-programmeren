from random import choice
#Vraag namen op van deelnemers (alle namen moeten uniek zijn).
#Bij minder dan 3 namen, blijf je doorvragen naar namen.
#Als er 3 namen ingevoerd zijn dan krijgt de gebruiker de optie om nog een naam in te voeren of kunnen er lootjes worden getrokken.
#Iedereen krijgt (random) één uniek lootje.
#Aan het einde mag niemand het lootje van zichzelf hebben.
#Als alles verdeeld is wordt er een lijst met namen geprint en de bijbehorende lootjes.
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
        break