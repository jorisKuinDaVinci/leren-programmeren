# EERST FUNCTIES, DAN

# VARIABELEN EN CONSTANTEN
OLIEBOL_PRIJS = 99
PRIJS_10_OLIEBOLLEN = 750
APPEPFLAP_PRIJS = 149

AANTAL_OLIEBOLLEN = 725
AANTAL_APPLEFLAPPEN = 0

aantal_zaken = AANTAL_OLIEBOLLEN // 10
aantal_losse = AANTAL_OLIEBOLLEN % 10
oliebollen_totaal = aantal_zaken * PRIJS_10_OLIEBOLLEN + aantal_losse * OLIEBOL_PRIJS

# BEREKENINGEN

prijs_totaal = oliebollen_totaal + AANTAL_APPLEFLAPPEN * APPEPFLAP_PRIJS
totaal_eur = prijs_totaal / 100   

print(f"De {AANTAL_OLIEBOLLEN} oliebollen en {AANTAL_APPLEFLAPPEN} appelflappen kosten samen: {totaal_eur}")