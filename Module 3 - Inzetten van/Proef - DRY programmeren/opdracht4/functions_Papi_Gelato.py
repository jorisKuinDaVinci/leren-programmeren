def vraag_aantal_bolletjes():
    return "Hoeveel bolletjes wilt u?"

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

def vraag_smaak(bolletje_nummer):
    return f"Welke smaak wilt u voor bolletje nummer {bolletje_nummer}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?"

def controleer_smaak(keuze):
    smaken = {"A": "Aardbei", "C": "Chocolade", "M": "Munt", "V": "Vanille"}
    return smaken.get(keuze.upper(), None)

def vraag_hoorntje_of_bakje(aantal):
    return f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?"

def controleer_keuze(keuze):
    if keuze.lower() in ["hoorntje", "bakje"]:
        return keuze.lower()
    else:
        return None

def vraag_topping():
    return "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?"

def controleer_topping(keuze):
    toppings = {
        "A": "Geen",
        "B": "Slagroom",
        "C": "Sprinkels",
        "D": "Caramel Saus",
    }
    return toppings.get(keuze.upper(), None)

def bereken_topping_prijs(topping, aantal_bolletjes, type_keuze):
    if topping == "Slagroom":
        return 0.50
    elif topping == "Sprinkels":
        return aantal_bolletjes * 0.30
    elif topping == "Caramel Saus":
        if type_keuze == "hoorntje":
            return 0.60
        elif type_keuze == "bakje":
            return 0.90
    else:
        return 0.0

def bevestiging_bestelling(keuze, aantal):
    return f"Hier is uw {keuze} met {aantal} bolletje(s)."

def vraag_nog_meer():
    return "Wilt u nog meer bestellen?"

def controleer_meer_bestellen(antwoord):
    if antwoord.lower() == "ja":
        return True
    elif antwoord.lower() == "nee":
        return False
    else:
        return None

def print_bon(bestellingen):
    print("\n---------[\"Papi Gelato\"]---------")
    totaal = 0.0

    # Smaken
    for smaak, aantal in bestellingen["smaken"].items():
        if aantal > 0:
            prijs = aantal * 1.10
            totaal += prijs
            print(f"B.{smaak:<10} {aantal:>3} x €1.10  = €{prijs:7.2f}")

    # Hoorntjes
    if bestellingen["hoorntjes"] > 0:
        naam = "Hoorntje" if bestellingen["hoorntjes"] == 1 else "Hoorntjes"
        prijs = bestellingen["hoorntjes"] * 1.25
        totaal += prijs
        print(f"{naam:<12} {bestellingen['hoorntjes']:>3} x €1.25  = €{prijs:7.2f}")

    # Bakjes
    if bestellingen["bakjes"] > 0:
        naam = "Bakje" if bestellingen["bakjes"] == 1 else "Bakjes"
        prijs = bestellingen["bakjes"] * 0.75
        totaal += prijs
        print(f"{naam:<12} {bestellingen['bakjes']:>3} x €0.75  = €{prijs:7.2f}")

    # Toppings (alleen weergeven als er toppings zijn)
    if bestellingen["topping_prijs"] > 0:
        print(f"Toppings     {'':>3}            = €{bestellingen['topping_prijs']:7.2f}")
        totaal += bestellingen["topping_prijs"]

    # Totaal
    print(f"{'':>31}--------- +")
    print(f"Totaal{'':>24}= €{totaal:7.2f}")
    print("\nBedankt en tot ziens!")
