# kosten van de feestlunch
#CROISSANTJES = 0.39
croissantjes = int(  float( input("Hoeveel kosten de croissantjes? ") )*100  )
#STOKBRODEN = 2.78
stokbroden = int(  float( input("Hoeveel kosten de stokbroden? ") )*100  )
#KORTINGSBONNEN = 0.50
kortingsbonnen = int(  float( input("Hoeveel kosten de kortingsbonnen? ") )*100  )
#aantal
AANTAL_CROISSANTJES = int(input("Hoeveel croissantjes wil je? "))
AANTAL_STOKBRODEN = int(input("Hoeveel stokbroden wil je? "))
AANTAL_KORTINGSBONNEN = int(input("Hoeveel kortingsbonnen heb je? "))
#prijs
prijs_croissantjes = AANTAL_CROISSANTJES * croissantjes
prijs_stokbroden = AANTAL_STOKBRODEN * stokbroden
prijs_kortingsbonnen = AANTAL_KORTINGSBONNEN * kortingsbonnen
#totaal
totaal = prijs_croissantjes + prijs_stokbroden - prijs_kortingsbonnen
print(f"De feestlunch kost je bij de bakker: {totaal:.2f} euro voor de {AANTAL_CROISSANTJES} croissantjes en de {AANTAL_STOKBRODEN} stokbroden als de {AANTAL_KORTINGSBONNEN} kortingsbonnen nog geldig zijn!")