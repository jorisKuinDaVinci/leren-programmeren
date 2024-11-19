def vraag_aantal(pizza_type):
    """Vraagt het aantal pizza's van een bepaald type op."""
    while True:
        try:
            return int(input(f"Hoeveel {pizza_type}? "))
        except ValueError:
            print("Dat is geen getal! Geef een cijfer.")

def bereken_kosten(aantallen, prijzen):
    """Bereken de kosten voor elke pizzatype en totaal."""
    kosten = {type_pizza: aantallen[type_pizza] * prijzen[type_pizza] for type_pizza in prijzen}
    totaal = sum(kosten[type_pizza] for type_pizza in kosten)
    return kosten, totaal

def print_overzicht(aantallen, kosten, totaal):
    """Print een overzicht van de bestelling."""
    print("----------------------------------------------------")
    for type_pizza, aantal in aantallen.items():
        print(f"|  {type_pizza.upper():<10}: {aantal}")
        print(f"|  Kosten {type_pizza:<7}: {kosten[type_pizza]:.2f}")
    print("----------------------------------------------------")
    print(f"|  Totaal: {totaal:.2f}")

PIZZA_PRIJZEN = {
    "klein": 5.00,
    "medium": 7.00,
    "groot": 10.00
}

# Vraag aantallen op
aantallen = {type_pizza: vraag_aantal(type_pizza) for type_pizza in PIZZA_PRIJZEN}

# Bereken kosten
kosten, totaal = bereken_kosten(aantallen, PIZZA_PRIJZEN)

# Print overzicht
print_overzicht(aantallen, kosten, totaal)