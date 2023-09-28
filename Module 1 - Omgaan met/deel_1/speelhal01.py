VIER_VRIENDEN = 7.45 * 4
PRIJS_PER_VIJF_MINUUT = 0.37
AANTAL_MINUTEN = 45
AANTAL_RONDJES = 9
gameseat_kosten = PRIJS_PER_VIJF_MINUUT * AANTAL_RONDJES

totaal = VIER_VRIENDEN + gameseat_kosten
#print(f"De totale kosten zijn: {totaal} euro")
if totaal > 0:
    #print(f"De totale kosten zijn: {totaal} euro")
    print(f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaal} euro')
elif totaal == 44.44:
    print(f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro')