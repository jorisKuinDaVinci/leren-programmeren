from data_Papi_Gelato import TEKSTEN, PRIJZEN, BTW_TARIEF

# Algemene invoercontrolefunctie
def vraag_invoer(vraag, validaties):
    """Stelt een vraag en controleert of de invoer geldig is volgens een set van validaties."""
    while True:
        print(vraag)
        keuze = input("> ").strip()
        for validatie in validaties:
            resultaat = validatie(keuze)
            if resultaat:
                return resultaat
        print("Sorry dat is geen optie die we aanbieden...")  # Nieuwe foutmelding

# Functie om het aantal bolletjes te vragen
def vraag_aantal_bolletjes():
    return "Hoeveel bolletjes wilt u?"

# Functie om het aantal bolletjes te controleren
def controleer_aantal_bolletjes(aantal):
    try:
        aantal = int(aantal)
        if 1 <= aantal <= 3:
            return "stap2", aantal
        elif 4 <= aantal <= 8:
            return "bakje", aantal
        elif aantal > 8:
            return "teveel", None
        else:
            return "ongeldig", None
    except ValueError:
        return "ongeldig", None

# Functie om een smaak voor een bolletje te vragen
def vraag_smaak(bolletje_nummer):
    return f"Welke smaak wilt u voor bolletje nummer {bolletje_nummer}? A) Aardbei, C) Chocolade of V) Vanille?"

# Functie om de smaak te controleren
def controleer_smaak(keuze):
    smaken = {"A": "Aardbei", "C": "Chocolade", "V": "Vanille"}  # Munt verwijderd
    return smaken.get(keuze.upper(), None)

# Vragen naar smaak met de algemene invoercontrolefunctie
def vraag_smaak_via_invoer(bolletje_nummer):
    return vraag_invoer(
        f"Welke smaak wilt u voor bolletje nummer {bolletje_nummer}? A) Aardbei, C) Chocolade, V) Vanille",
        [controleer_smaak]
    )

# Functie om te vragen of de klant een hoorntje of bakje wil
def vraag_hoorntje_of_bakje(aantal):
    return f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?"

# Functie om de keuze tussen hoorntje of bakje te controleren
def controleer_keuze(keuze):
    if keuze.lower() in ["hoorntje", "bakje"]:
        return keuze.lower()
    return None

# Vragen naar keuze met de algemene invoercontrolefunctie
def vraag_hoorntje_of_bakje_via_invoer():
    return vraag_invoer(
        "Wilt u uw ijsje in een hoorntje of een bakje?",
        [controleer_keuze]
    )

# Functie om een topping te vragen
def vraag_topping():
    return "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?"

# Functie om de topping te controleren
def controleer_topping(keuze):
    toppings = {
        "A": "Geen",
        "B": "Slagroom",
        "C": "Sprinkels",
        "D": "Caramel Saus",
    }
    return toppings.get(keuze.upper(), None)

# Vragen naar topping met de algemene invoercontrolefunctie
def vraag_topping_via_invoer():
    return vraag_invoer(
        "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels, D) Caramel Saus?",
        [controleer_topping]
    )

# Functie om de prijs van de topping te berekenen
def bereken_topping_prijs(topping, aantal_bolletjes, type_keuze):
    topping_prijzen = PRIJZEN["toppings"]
    if topping == "Sprinkels":
        return aantal_bolletjes * topping_prijzen["Sprinkels"]
    if topping == "Caramel Saus":
        return topping_prijzen[f"Caramel Saus {type_keuze.capitalize()}"]
    return topping_prijzen.get(topping, 0.0)

# Functie om de bestelling te bevestigen
def bevestiging_bestelling(keuze, aantal):
    return f"Hier is uw {keuze} met {aantal} bolletje(s)."

# Functie om de bon af te drukken
def print_bon(bestellingen, klant_type):
    print("\n---------[\"Papi Gelato\"]---------")
    totaal = 0.0

    # Smaken
    for smaak, aantal in bestellingen["smaken"].items():
        if aantal > 0:
            prijs_per_eenheid = PRIJZEN["liter"] if klant_type == "zakelijk" else PRIJZEN["bolletje"]
            prijs = aantal * prijs_per_eenheid
            totaal += prijs
            L_of_B = "L." if klant_type == "zakelijk" else "B."
            print(f"{L_of_B}{smaak:<10} {aantal:>3} x €{prijs_per_eenheid:4.2f}  = €{prijs:7.2f}")

    # Alleen particulier: Hoorntjes en Bakjes
    if klant_type == "particulier":
        if bestellingen["hoorntjes"] > 0:
            naam = "Hoorntje" if bestellingen["hoorntjes"] == 1 else "Hoorntjes"
            prijs = bestellingen["hoorntjes"] * PRIJZEN["hoorntje"]
            totaal += prijs
            print(f"{naam:<12} {bestellingen['hoorntjes']:>3} x €{PRIJZEN['hoorntje']:4.2f}  = €{prijs:7.2f}")

        if bestellingen["bakjes"] > 0:
            naam = "Bakje" if bestellingen["bakjes"] == 1 else "Bakjes"
            prijs = bestellingen["bakjes"] * PRIJZEN["bakje"]
            totaal += prijs
            print(f"{naam:<12} {bestellingen['bakjes']:>3} x €{PRIJZEN['bakje']:4.2f}  = €{prijs:7.2f}")

        if bestellingen["topping_prijs"] > 0:
            print(f"Toppings     {'':>3}            = €{bestellingen['topping_prijs']:7.2f}")
            totaal += bestellingen["topping_prijs"]

    # Totaal
    print(f"{'':>27}--------- +")
    print(f"Totaal{'':>20}= €{totaal:7.2f}")

    if klant_type == "zakelijk":
        btw = totaal * BTW_TARIEF["standaard"]
        print(f"BTW ({BTW_TARIEF['standaard'] * 100:.0f}%) {'':>17}= €{btw:7.2f}")

    print("\nBedankt en tot ziens!")

# Functie voor het klanttype te vragen
def vraag_klant_type():
    return "Bent u 1) een particuliere klant of 2) een zakelijke klant?"

# Functie om het klanttype te controleren
def controleer_klant_type(keuze):
    if keuze == "1":
        return "particulier"
    elif keuze == "2":
        return "zakelijk"
    return None

# Vragen naar klanttype met de algemene invoercontrolefunctie
def vraag_klant_type_via_invoer():
    return vraag_invoer(
        "Bent u 1) een particuliere klant of 2) een zakelijke klant?",
        [controleer_klant_type]
    )

# Functie voor zakelijke klant workflow
def zakelijke_klant_workflow(bestellingen):
    print("Zakelijke klant gekozen.")
    
    # Vraag het aantal liters
    while True:
        print("Hoeveel liter wilt u bestellen?")
        keuze = input("> ").strip()
        try:
            liters = int(keuze)
            if liters > 0:
                bestellingen["liters"] = liters
                break
            else:
                print("Sorry, dat aantal begrijp ik niet. Probeer opnieuw.")
        except ValueError:
            print("Sorry, dat aantal begrijp ik niet. Probeer opnieuw.")
    
    # Vraag naar de smaken en voeg ze toe
    for i in range(1, liters + 1):
        smaak = vraag_invoer(
            f"Welke smaak wilt u voor liter nummer {i}? A) Aardbei, C) Chocolade, V) Vanille?",
            [controleer_smaak]
        )
        bestellingen["smaken"][smaak] += 1
    # Print de bon
    print_bon(bestellingen, "zakelijk")

# Functie voor particuliere klant workflow
def particulier_workflow(bestellingen):
    print("Particuliere klant gekozen.")
    
    # Vraag het aantal bolletjes
    print(vraag_aantal_bolletjes())
    keuze = input("> ")
    status, aantal_bolletjes = controleer_aantal_bolletjes(keuze)
    
    if status == "teveel":
        print(TEKSTEN["teveel_bolletjes"])
        return
    
    # Voeg het aantal bolletjes toe aan de bestelling
    bestellingen["bolletjes"] = aantal_bolletjes
    
    # Vraag naar de smaken en voeg ze toe
    for i in range(1, aantal_bolletjes + 1):

        # Vraag naar de smaak
        smaak = vraag_smaak_via_invoer(1)  # Voor bolletje nummer 1
        if smaak:
            bestellingen["smaken"][smaak] += 1
    
    # Vraag naar hoorntje of bakje
    type_keuze = vraag_hoorntje_of_bakje_via_invoer()
    
    if type_keuze == "hoorntje":
        bestellingen["hoorntjes"] = aantal_bolletjes
    elif type_keuze == "bakje":
        bestellingen["bakjes"] = aantal_bolletjes
    
    # Vraag naar de topping
    topping = vraag_topping_via_invoer()
    
    if topping:
        bestellingen["topping_prijs"] = bereken_topping_prijs(topping, aantal_bolletjes, type_keuze)
    
    # Bevestig de bestelling
    print(bevestiging_bestelling(type_keuze, aantal_bolletjes))
    
    # Print de bon
    print_bon(bestellingen, "particulier")