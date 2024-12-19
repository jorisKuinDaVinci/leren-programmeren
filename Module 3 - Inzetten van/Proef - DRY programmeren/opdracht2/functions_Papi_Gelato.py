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

def vraag_hoorntje_of_bakje(aantal):
    return f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?"

def controleer_keuze(keuze):
    if keuze.lower() in ["hoorntje", "bakje"]:
        return keuze.lower()
    else:
        return None

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

    if bestellingen["bolletjes"] > 0:
        prijs = 1.10
        bedrag = bestellingen["bolletjes"] * prijs
        totaal += bedrag
        print(f"Bolletjes {bestellingen['bolletjes']:>3} x €{prijs:5.2f} = €{bedrag:6.2f}")

    if bestellingen["hoorntjes"] > 0:
        prijs = 1.25
        bedrag = bestellingen["hoorntjes"] * prijs
        totaal += bedrag
        print(f"Hoorntjes {bestellingen['hoorntjes']:>3} x €{prijs:5.2f} = €{bedrag:6.2f}")

    if bestellingen["bakjes"] > 0:
        prijs = 0.75
        bedrag = bestellingen["bakjes"] * prijs
        totaal += bedrag
        print(f"Bakjes    {bestellingen['bakjes']:>3} x €{prijs:5.2f} = €{bedrag:6.2f}")

    print(f"{'':>23}--------- +")
    print(f"Totaal{'':>16} = €{totaal:6.2f}")
    print("\nBedankt en tot ziens!")