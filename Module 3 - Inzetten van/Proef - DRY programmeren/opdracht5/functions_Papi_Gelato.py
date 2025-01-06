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
    if topping == "Geen":
        return 0.0
    elif topping == "Slagroom":
        return 0.50
    elif topping == "Sprinkels":
        return aantal_bolletjes * 0.30
    elif topping == "Caramel Saus":
        return 0.60 if type_keuze == "hoorntje" else 0.90
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
    return None

def vraag_en_verwerk_smaken(aantal, bestellingen, vraag_smaak, controleer_smaak):
    """
    Vraagt naar smaken en verwerkt deze in de bestellingen.
    """
    for i in range(1, aantal + 1):
        while True:
            print(vraag_smaak(i))
            smaak = input("> ")
            gekozen_smaak = controleer_smaak(smaak)
            if gekozen_smaak:
                bestellingen["smaken"][gekozen_smaak] += 1
                break
            else:
                print("Sorry dat snap ik niet...")

def vraag_en_verwerk_topping(aantal, keuze, bestellingen, vraag_topping, controleer_topping, bereken_topping_prijs):
    """
    Vraagt naar toppings en verwerkt de prijs in de bestellingen.
    """
    while True:
        print(vraag_topping())
        topping = input("> ")
        gekozen_topping = controleer_topping(topping)
        if gekozen_topping:
            topping_prijs = bereken_topping_prijs(gekozen_topping, aantal, keuze)
            bestellingen["topping_prijs"] += topping_prijs
            break
        else:
            print("Sorry dat snap ik niet...")

def print_bon(bestellingen, klant_type):
    print("\n---------[\"Papi Gelato\"]---------")
    totaal = 0.0

    # Smaken
    for smaak, aantal in bestellingen["smaken"].items():
        if aantal > 0:
            prijs_per_eenheid = 9.80 if klant_type == "zakelijk" else 1.10
            prijs = aantal * prijs_per_eenheid
            totaal += prijs
            prefix = "L." if klant_type == "zakelijk" else "B."
            print(f"{prefix}{smaak:<10} {aantal:>3} x €{prijs_per_eenheid:4.2f}  = €{prijs:7.2f}")

    # Alleen particulier: Hoorntjes en Bakjes
    if klant_type == "particulier":
        if bestellingen["hoorntjes"] > 0:
            naam = "Hoorntje" if bestellingen["hoorntjes"] == 1 else "Hoorntjes"
            prijs = bestellingen["hoorntjes"] * 1.25
            totaal += prijs
            print(f"{naam:<12} {bestellingen['hoorntjes']:>3} x €1.25  = €{prijs:7.2f}")

        if bestellingen["bakjes"] > 0:
            naam = "Bakje" if bestellingen["bakjes"] == 1 else "Bakjes"
            prijs = bestellingen["bakjes"] * 0.75
            totaal += prijs
            print(f"{naam:<12} {bestellingen['bakjes']:>3} x €0.75  = €{prijs:7.2f}")

        if bestellingen["topping_prijs"] > 0:
            print(f"Toppings     {'':>3}            = €{bestellingen['topping_prijs']:7.2f}")
            totaal += bestellingen["topping_prijs"]

    # Totaal en BTW
    print(f"{'':>31}--------- +")
    print(f"Totaal{'':>24}= €{totaal:7.2f}")

    if klant_type == "zakelijk":
        btw = totaal * 0.09  # 9% BTW
        print(f"BTW (9%){'':>21}= €{btw:7.2f}")

    print("\nBedankt en tot ziens!")

def vraag_klant_type():
    return "Bent u 1) een particuliere klant of 2) een zakelijke klant?"

def controleer_klant_type(keuze):
    if keuze == "1":
        return "particulier"
    elif keuze == "2":
        return "zakelijk"
    return None

def zakelijke_klant_workflow(bestellingen):
    while True:
        try:
            print("Hoeveel liter wilt u?")
            aantal_liter = int(input("> "))
            if aantal_liter <= 0:
                print("Voer een geldig aantal liters in.")
                continue
            elif aantal_liter > 100:
                print("Sorry, we kunnen maximaal 100 liter per bestelling verwerken.")
                continue
            break
        except ValueError:
            print("Sorry dat snap ik niet...")
    
    for i in range(1, aantal_liter + 1):
        while True:
            print(f"Welke smaak wilt u voor liter nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            smaak = input("> ")
            gekozen_smaak = controleer_smaak(smaak)
            if gekozen_smaak:
                bestellingen["smaken"][gekozen_smaak] += 1
                break
            else:
                print("Sorry dat snap ik niet...")

    print_bon(bestellingen, klant_type="zakelijk")
    exit()

def particulier_workflow(bestellingen):
    """
    Behandelt de workflow voor particuliere klanten.
    """
    print(vraag_aantal_bolletjes())
    aantal_input = input("> ")
    status, aantal = controleer_aantal_bolletjes(aantal_input)

    if status == "stap2":
        vraag_en_verwerk_smaken(aantal, bestellingen, vraag_smaak, controleer_smaak)

        while True:
            print(vraag_hoorntje_of_bakje(aantal))
            keuze = input("> ")
            keuze = controleer_keuze(keuze)
            if keuze:
                print(bevestiging_bestelling(keuze, aantal))
                bestellingen["bolletjes"] += aantal
                if keuze == "hoorntje":
                    bestellingen["hoorntjes"] += 1
                elif keuze == "bakje":
                    bestellingen["bakjes"] += 1
                vraag_en_verwerk_topping(
                    aantal, keuze, bestellingen, vraag_topping, controleer_topping, bereken_topping_prijs
                )
                break
            else:
                print("Sorry, dat snap ik niet...")