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
if totaal > 0:
    print(f"De feestlunch kost je bij de bakker: {totaal} euro")
elif totaal == 18.88:
    print(f'De feestlunch kost je bij de bakker 18.88 euro voor de {AANTAL_CROISSANTJES} croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')
