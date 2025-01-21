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

def grabbel_ballen(huidig_team, bingokaart_team, groene_ballen, rode_ballen):
    """
    Trek ballen en update de bingokaart voor het huidige team.
    """
    ballen = ["groen", "rood"]
    gekozen_ballen = random.sample(ballen, 1)

    if gekozen_ballen[0] == "groen":
        groene_ballen += 1
        print(f"{huidig_team} heeft een groene bal!")
        # Markeer een willekeurige plek als "x"
        for i in range(5):
            for j in range(5):
                if bingokaart_team[i][j] == "_":
                    bingokaart_team[i][j] = "x"
                    return groene_ballen, rode_ballen, True
    elif gekozen_ballen[0] == "rood":
        rode_ballen += 1
        print(f"{huidig_team} heeft een rode bal!")
        return groene_ballen, rode_ballen, False

    return groene_ballen, rode_ballen, False