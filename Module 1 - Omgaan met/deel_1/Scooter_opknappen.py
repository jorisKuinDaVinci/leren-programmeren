#je scooter mankeert van alles. En kan een opknapbeurt gebruiken:

#de 2 banden zijn versleten
#de 2 lampjes moeten vervangen
#Kan je dat betalen?

#Een nieuwe band kost: € 57,79

#Arbeid per band kost: € 15,00

#Een nieuw lampje kost: € 1,45

#Lampjes vervangen per lampje kost: €2,10

#Opdracht:
#Maak een programma scooter.py dat de kosten kan uitrekenen.
#Gebruik variabelen voor alle gegevens.
#Gebruik duidelijke variabelenamen

NIEUWE_BAND = 57.79
ARBEID_PER_BAND = 15.00
NIEUW_LAMPJE = 1.45
LAMPJES_VERVANGEN_PER_LAMPJE = 2.10

AANTAL_LAMPJES = 2
AANTAL_BANDEN = 2

prijs_lampjes = NIEUW_LAMPJE * AANTAL_LAMPJES
prijs_banden = NIEUWE_BAND * AANTAL_BANDEN
lampjes_vervangen_prijs = LAMPJES_VERVANGEN_PER_LAMPJE * AANTAL_LAMPJES
arbeid_banden_prijs = ARBEID_PER_BAND * AANTAL_BANDEN
totaal_lampjes = prijs_lampjes + lampjes_vervangen_prijs
totaal_banden = prijs_banden + arbeid_banden_prijs
totaal = totaal_lampjes + totaal_banden
print(f"de scooter opknappen kost: {totaal}")