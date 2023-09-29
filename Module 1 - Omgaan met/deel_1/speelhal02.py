AANTAL_MENSEN = 4
PERSOONS_PRIJS = 7.45
PRIJS_PER_VIJF_MINUUT = 0.37
AANTAL_MINUTEN = 45
AANTAL_RONDJES = 9
#totaal_kosten_gameseat = ((TIJD_GAMESEAT_MINUTEN / 5) * PRIJS_PER_VIJF_MINUUT) * AANTAL_MENSEN
totaal_kosten_gameseat = ((AANTAL_MINUTEN / 5) * PRIJS_PER_VIJF_MINUUT) * AANTAL_MENSEN
persoons_kosten = PERSOONS_PRIJS * AANTAL_MENSEN
# 45 minuten VR kost 9 rondjes van 5 minuten
#gameseat_kosten = PRIJS_PER_VIJF_MINUUT * AANTAL_RONDJES

totaal = persoons_kosten + totaal_kosten_gameseat
#print(f"De totale kosten zijn: {totaal} euro")
if totaal > 0:
    #print(f"De totale kosten zijn: {totaal} euro")
    print(f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaal} euro')
elif totaal == 44.44:
    print(f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro')