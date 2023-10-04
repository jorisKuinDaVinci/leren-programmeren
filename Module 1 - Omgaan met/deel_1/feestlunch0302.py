# kosten van de feestlunch
CROISSANTJES = 0.39
STOKBRODEN = 2.78
KORTINGSBONNEN = 0.50
#aantal
AANTAL_CROISSANTJES = 17
AANTAL_STOKBRODEN = 2
AANTAL_KORTINGSBONNEN = 3
#prijs
prijs_croissantjes = AANTAL_CROISSANTJES * CROISSANTJES
prijs_stokbroden = AANTAL_STOKBRODEN * STOKBRODEN
prijs_kortingsbonnen = AANTAL_KORTINGSBONNEN * KORTINGSBONNEN
#totaal
totaal = prijs_croissantjes + prijs_stokbroden - prijs_kortingsbonnen
print(f"De feestlunch kost je bij de bakker: {totaal} euro voor de {AANTAL_CROISSANTJES} croissantjes en de {AANTAL_STOKBRODEN} stokbroden als de {AANTAL_KORTINGSBONNEN} kortingsbonnen nog geldig zijn!")