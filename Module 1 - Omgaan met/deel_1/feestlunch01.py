CROISSANTJES = 0.39
#print(type(CROISSANTJES)) laat zien wat voor type het is
STOKBRODEN = 2.78
#totaal = 17 * croissantjes + 2 * stokbroden
KORTINGSBONNEN = 0.50
totaal = 17 * CROISSANTJES + 2 * STOKBRODEN - 3 * KORTINGSBONNEN
if totaal > 0:
    print(f"De totale kosten zijn: {totaal} euro")
elif totaal == 18.88:
    print(f'De feestlunch kost je bij de bakker 18.88 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')
