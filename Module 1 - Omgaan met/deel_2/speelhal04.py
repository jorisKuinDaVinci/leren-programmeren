#AANTAL_MENSEN = 4
AANTAL_MENSEN = int(input("Hoeveel mensen gaan er mee? "))
#PERSOONS_PRIJS = 7.45
PERSOONS_PRIJS = int(  float( input("Hoeveel kost een persoon? ") )*100  )
#PRIJS_PER_VIJF_MINUUT = 0.37
PRIJS_PER_VIJF_MINUUT = int(  float( input("Hoeveel kost 5 minuten? ") )*100  )
#AANTAL_MINUTEN = 45
AANTAL_MINUTEN = int(input("Hoeveel minuten gaan jullie? "))

totaal_kosten_gameseat = ((AANTAL_MINUTEN / 5) * PRIJS_PER_VIJF_MINUUT) * AANTAL_MENSEN

persoons_kosten = PERSOONS_PRIJS * AANTAL_MENSEN
# 45 minuten VR kost 9 rondjes van 5 minuten

totaal = persoons_kosten + totaal_kosten_gameseat
print(f'Dit geweldige dagje-uit met {AANTAL_MENSEN} mensen in de Speelhal met {AANTAL_MINUTEN} minuten VR kost je maar {totaal:.2f} euro')