# kosten van de feestlunch
CROISSANTJES = input("Wat kosten de croissantjes?") #= 0.39
STOKBRODEN = input("Wat kosten de stokbroden?") #= 2.78
KORTINGSBONNEN = input("Wat kosten de kortingsbonnen?") #= 0.50
#aantal
AANTAL_CROISSANTJES = input("Hoeveel croissantjes wil je?") #= 17
AANTAL_STOKBRODEN = input("Hoeveel stokbroden wil je?") #= 2
AANTAL_KORTINGSBONNEN = input("Hoeveel kortingsbonnen wil je?") #= 3
#prijs
prijs_croissantjes = AANTAL_CROISSANTJES * CROISSANTJES
prijs_stokbroden = AANTAL_STOKBRODEN * STOKBRODEN
prijs_kortingsbonnen = AANTAL_KORTINGSBONNEN * KORTINGSBONNEN
#totaal
totaal = prijs_croissantjes + prijs_stokbroden - prijs_kortingsbonnen
print(f"De feestlunch kost je bij de bakker: {totaal} euro")