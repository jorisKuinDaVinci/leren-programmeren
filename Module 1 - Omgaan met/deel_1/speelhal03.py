AANTAL_MENSEN = input("Hoeveel mensen?") #= 4
PERSOONS_PRIJS = input("Hoeveel kost een persoon?") #= 7.45
PRIJS_PER_VIJF_MINUUT = input("Hoeveel kost een vijf minuten?") #= 0.37
AANTAL_MINUTEN = input("Hoeveel minuten?") #= 45
AANTAL_RONDJES = input("Hoeveel rondjes?") #= 9

totaal_kosten_gameseat = ((AANTAL_MINUTEN / 5) * PRIJS_PER_VIJF_MINUUT) * AANTAL_MENSEN

persoons_kosten = PERSOONS_PRIJS * AANTAL_MENSEN
# 45 minuten VR kost 9 rondjes van 5 minuten

totaal = persoons_kosten + totaal_kosten_gameseat
print(f'Dit geweldige dagje-uit met {AANTAL_MENSEN} mensen in de Speelhal met {AANTAL_MINUTEN} minuten VR kost je maar {totaal} euro')