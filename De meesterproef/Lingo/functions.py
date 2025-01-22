import random
from termcolor import colored

def kies_willekeurig_woord(woordenlijst):
    """Kies een willekeurig woord uit de woordenlijst."""
    return random.choice(woordenlijst)

def controleer_letters(te_raden_woord, invoer, geraden_letters, geraden_letters_zonder_kleur):
    """
    Controleer geraden letters tegen het te raden woord.
    """
    # Itereer door elk teken van het geraden woord
    for i in range(len(te_raden_woord)):
        if invoer[i] == te_raden_woord[i]:
            # Letter is correct en op de juiste positie
            geraden_letters[i] = colored(te_raden_woord[i], "green")  # Groen
            geraden_letters_zonder_kleur[i] = te_raden_woord[i]  # Bewaar de letter zonder kleur voor vergelijking
        elif invoer[i] in te_raden_woord and geraden_letters_zonder_kleur[i] == "_":
            # Letter is in het woord, maar op de verkeerde positie
            geraden_letters[i] = colored(invoer[i], "yellow")  # Geel
            geraden_letters_zonder_kleur[i] = invoer[i]  # Bewaar de letter zonder kleur voor vergelijking
        elif geraden_letters_zonder_kleur[i] == "_":
            # Letter is onjuist en blijft een underscore
            geraden_letters[i] = "_"
            geraden_letters_zonder_kleur[i] = "_"

def raad_woord(te_raden_woord, geraden_letters, max_beurten=5):
    """
    Laat de gebruiker proberen het woord te raden.
    Beperk het aantal beurten tot max_beurten (standaard 5).
    """
    # Maak een lijst van letters zonder kleurcodes voor vergelijking
    geraden_letters_zonder_kleur = ["_"] * len(te_raden_woord)
    
    for poging_nummer in range(1, max_beurten + 1):  # Beperk tot max_beurten pogingen
        print(f"Poging {poging_nummer} van {max_beurten}:")
        invoer = input("Raad het woord: ").strip().lower()
        
        # Controleer of het woord de juiste lengte heeft
        if len(invoer) != len(te_raden_woord):
            print(f"Fout: het woord moet {len(te_raden_woord)} letters lang zijn.")
            continue

        # Controleer letters en toon resultaat
        controleer_letters(te_raden_woord, invoer, geraden_letters, geraden_letters_zonder_kleur)

        # Toon de huidige status van geraden letters
        print("Huidige voortgang: " + "".join(geraden_letters))

        # Controleer of het woord volledig geraden is
        if "".join(geraden_letters_zonder_kleur) == te_raden_woord:
            print("Gefeliciteerd! Je hebt het woord geraden.")
            return True
        else:
            print("Niet correct, probeer het opnieuw.")
    print(f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}")
    return False

def toon_te_raden_woord(speler_naam, te_raden_woord):
    """Toon het te raden woord als de speler 'Joris' heet."""
    if speler_naam.lower() == "joris":
        print(f"[DEBUG] Het te raden woord is: {te_raden_woord}")

def bingokaart():
    """Genereer een lege bingokaart (5x5)."""
    return [["_" for _ in range(5)] for _ in range(5)]

def print_bingokaart(kaart):
    """Print een bingokaart netjes uit."""
    print("Bingokaart:")
    for rij in kaart:
        print(" ".join(rij))

def check_bingo(kaart):
    """Controleer of er bingo is (volledige rij of kolom)."""
    # Controleer rijen
    for rij in kaart:
        if all(v == "x" for v in rij):
            return True
    # Controleer kolommen
    for col in range(5):
        if all(kaart[rij][col] == "x" for rij in range(5)):
            return True
    return False

def grabbel_ballen(team, bingokaart, ballenbak, groene_ballen, rode_ballen):
    """
    Simuleer het grabbelen van ballen en pas de bijbehorende actie toe.
    """
    while True:
        print(f"{team} grabbelt een bal...")
        if not ballenbak:
            print("De ballenbak is leeg!")
            return groene_ballen, rode_ballen, False

        # Trek een bal uit de ballenbak
        bal = random.choice(ballenbak)
        ballenbak.remove(bal)

        if bal == "groen":
            groene_ballen += 1
            print(f"{team} trekt een groene bal! Je hebt nu {groene_ballen} groene bal(len).")
            if groene_ballen == 3:
                print(f"{team} heeft 3 groene ballen en wint de jackpot!")
                return groene_ballen, rode_ballen, False
            # Groene bal: mag nog een keer trekken, blijf in de lus

        elif bal == "rood":
            rode_ballen += 1
            print(f"{team} trekt een rode bal! De beurt gaat naar het andere team.")
            return groene_ballen, rode_ballen, False  # Beurt eindigt bij een rode bal

        elif bal == "?":
            print(f"{team} trekt het vraagteken! Kies een getal op de bingokaart om af te strepen.")
            # Vraag speler om een getal te kiezen
            while True:
                try:
                    keuze = int(input("Welk getal wil je afstrepen? (1-25): "))
                    if 1 <= keuze <= 25:
                        rij = (keuze - 1) // 5  # Bereken de rij
                        kolom = keuze - 1 - (rij * 5)  # Bereken de kolom
                        if bingokaart[rij][kolom] == "_":
                            bingokaart[rij][kolom] = "X"
                            print(f"Getal {keuze} afgestreept op de bingokaart!")
                            break
                        else:
                            print("Dit getal is al afgestreept. Kies een ander getal.")
                    else:
                        print("Voer een geldig getal in tussen 1 en 25.")
                except ValueError:
                    print("Voer een geldig nummer in.")
        else:
            print(f"{team} trekt een blauwe bal met nummer {bal}.")
            # Blauwe bal: markeer het nummer op de kaart
            rij = (bal - 1) // 5  # Bereken de rij
            kolom = bal - 1 - (rij * 5)  # Bereken de kolom
            if bingokaart[rij][kolom] == "_":
                bingokaart[rij][kolom] = "X"
                print(f"Nummer {bal} afgestreept op de bingokaart.")
            else:
                print(f"Nummer {bal} was al afgestreept.")

        # Vraag of het team door wil gaan
        doorgaan = input("Wil je nog een bal trekken? (ja/nee): ").strip().lower()
        if doorgaan != "ja":
            return groene_ballen, rode_ballen, True