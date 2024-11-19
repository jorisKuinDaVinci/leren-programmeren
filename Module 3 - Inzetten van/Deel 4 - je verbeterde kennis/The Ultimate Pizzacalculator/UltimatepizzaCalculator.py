PIZZA_PRIJZEN = {
    "klein": 5.00,
    "medium": 7.00,
    "groot": 10.00
}

# Vraag aantallen op
aantallen = {}
for type_pizza in PIZZA_PRIJZEN:
    while True:
        try:
            aantallen[type_pizza] = int(input(f"Hoeveel {type_pizza}? "))
            break
        except ValueError:
            print("Dat is geen getal! Geef een cijfer.")

# Bereken kosten
kosten = {type_pizza: aantallen[type_pizza] * PIZZA_PRIJZEN[type_pizza] for type_pizza in PIZZA_PRIJZEN}
totaal = sum(kosten[type_pizza] for type_pizza in kosten)

# Print overzicht
print("----------------------------------------------------")
for type_pizza, aantal in aantallen.items():
    # Handmatig de eerste letter van het type pizza hoofdletter maken
    pizza_naam = type_pizza[0].upper() + type_pizza[1:]
    print(f"|  {pizza_naam:<10}: {aantal}")
    print(f"|  Kosten {type_pizza:<7}: {kosten[type_pizza]:.2f}")
print("----------------------------------------------------")
print(f"|  Totaal: {totaal:.2f}")