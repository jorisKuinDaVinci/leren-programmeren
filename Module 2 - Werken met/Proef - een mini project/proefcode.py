from random import random

vraag_naam = input("geef een naam: ")
vraag_naam2 = input("geef een naam: ")
vraag_naam3 = input("geef een naam: ")

wil_je_nog_een_naam = input("wil je nog een naam geven? ")
if wil_je_nog_een_naam == "ja":
    vraag_naam4 = input("geef een naam: ")
else:
    print("oke, geen naam meer")

if wil_je_nog_een_naam == "ja":
    namen = [vraag_naam, vraag_naam2, vraag_naam3, vraag_naam4]
else:
    namen = [vraag_naam, vraag_naam2, vraag_naam3]

# van de opgegeven namen wordt er een willekeurige naam gekozen.
# iedereen krijgt een naam van een ander persoon. 
# een naam mag niet twee keer gekozen worden.
# je mag niet je eigen naam krijgen.

persoon1_krijgt = namen[int(random() * len(namen))]
namen.remove(persoon1_krijgt)
persoon2_krijgt = namen[int(random() * len(namen))]
namen.remove(persoon2_krijgt)
persoon3_krijgt = namen[int(random() * len(namen))]
namen.remove(persoon3_krijgt)
if wil_je_nog_een_naam == "ja":
    persoon4_krijgt = namen[int(random() * len(namen))]
    namen.remove(persoon4_krijgt)
else:
    print("oke, geen naam meer")

print(f"{vraag_naam} krijgt de naam van {persoon1_krijgt}")
print(f"{vraag_naam2} krijgt de naam van {persoon2_krijgt}")
print(f"{vraag_naam3} krijgt de naam van {persoon3_krijgt}")
if wil_je_nog_een_naam == "ja":
    print(f"{vraag_naam4} krijgt de naam van {persoon4_krijgt}")
else:
    print("oke, geen naam meer")

