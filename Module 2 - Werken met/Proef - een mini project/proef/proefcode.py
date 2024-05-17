from random import choice

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

def random_naam(namen):
    random_naam = choice(namen)
    if random_naam == vraag_naam:
        random_naam = choice(namen)   
    return random_naam

def random_naam2(namen):
    random_naam2 = choice(namen)
    if random_naam2 == vraag_naam2:
        random_naam2 = choice(namen)
    return random_naam2

def random_naam3(namen):
    random_naam3 = choice(namen)
    if random_naam3 == vraag_naam3:
        random_naam3 = choice(namen)
    return random_naam3

def random_naam4(namen):
    random_naam4 = choice(namen)
    if random_naam4 == vraag_naam4:
        random_naam4 = choice(namen)
    return random_naam4

persoon1_krijgt = random_naam(namen)
persoon2_krijgt = random_naam2(namen)
persoon3_krijgt = random_naam3(namen)
if wil_je_nog_een_naam == "ja":
    persoon4_krijgt = random_naam4(namen)

persoon1_krijgt_print = print(f"{vraag_naam} krijgt de naam van {persoon1_krijgt}")
persoon2_krijgt_print = print(f"{vraag_naam2} krijgt de naam van {persoon2_krijgt}")
persoon3_krijgt_print = print(f"{vraag_naam3} krijgt de naam van {persoon3_krijgt}")
if wil_je_nog_een_naam == "ja":
    persoon4_krijgt_print = print(f"{vraag_naam4} krijgt de naam van {persoon4_krijgt}")