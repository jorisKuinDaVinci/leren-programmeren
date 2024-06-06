#je scooter mankeert van alles. En kan een opknapbeurt gebruiken:

#de 2 banden zijn versleten
#de 2 lampjes moeten vervangen
#Kan je dat betalen?

#Een nieuwe band kost: € 57,79

#Arbeid per band kost: € 15,00

#Een nieuw lampje kost: € 1,45

#Lampjes vervangen per lampje kost: €2,10

#Opdracht:
#Maak een programma scooter-input.py dat de kosten kan uitrekenen.
#Gebruik variabelen voor alle gegevens.
#Laat alle gegevens invoeren en converteren naar int of float
#Geef in de input prompt aan wat de standaard prijs is. Bijvoorbeeld:
#Bandenprijs (€ 57.79) Nu?
#Gebruik duidelijke variabelenamen
NIEUWE_BAND = 57.79
nieuwe_band_tekst = f"Bandenprijs (€ {NIEUWE_BAND}) Nu?"
ARBEID_PER_BAND = 15.00
arbeid_per_band_tekst = f"Arbeid per band prijs (€ {ARBEID_PER_BAND}) Nu?"
NIEUW_LAMPJE = 1.45
nieuw_lampje_tekst = f"Lampjesprijs (€ {NIEUW_LAMPJE}) Nu?"
LAMPJES_VERVANGEN_PER_LAMPJE = 2.10
lampjes_vervangen_per_lampje_tekst = f"Lampjes vervangen prijs (€ {LAMPJES_VERVANGEN_PER_LAMPJE}) Nu?"


nieuwe_band_input = float(input(nieuwe_band_tekst))
arbeid_per_band_input = float(input(arbeid_per_band_tekst))
nieuw_lampje_input = float(input(nieuw_lampje_tekst))
lampjes_vervangen_per_lampje_input = float(input(lampjes_vervangen_per_lampje_tekst))

AANTAL_LAMPJES = 2
AANTAL_BANDEN = 2

prijs_lampjes = nieuw_lampje_input * AANTAL_LAMPJES
prijs_banden = nieuwe_band_input * AANTAL_BANDEN
lampjes_vervangen_prijs = lampjes_vervangen_per_lampje_input * AANTAL_LAMPJES
arbeid_banden_prijs = arbeid_per_band_input * AANTAL_BANDEN
totaal_lampjes = prijs_lampjes + lampjes_vervangen_prijs
totaal_banden = prijs_banden + arbeid_banden_prijs
totaal = totaal_lampjes + totaal_banden
print(f"de scooter opknappen kost: {totaal}")