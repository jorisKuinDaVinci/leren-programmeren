import random
from termcolor import colored

from teksten import (
    print_geraden,
    print_verkeerd_geraden,
    print_helaas_geraden_woord,
    print_fout_woord_lengte
)


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


def raad_woord(te_raden_woord, geraden_letters):
    """
    Laat de gebruiker proberen het woord te raden, met maximaal 5 pogingen.
    """
    # Maak een lijst van letters zonder kleurcodes voor vergelijking
    geraden_letters_zonder_kleur = ["_"] * len(te_raden_woord)
    pogingen = 0  # Teller voor het aantal pogingen
    
    while pogingen < 5:  # Maximaal 5 pogingen
        # Vraag gebruiker om een woord te raden
        invoer = input(f"Poging {pogingen + 1} van 5. Raad het woord: ").strip().lower()
        
        # Controleer of het woord de juiste lengte heeft
        if len(invoer) != len(te_raden_woord):
            print_fout_woord_lengte(te_raden_woord)  # Gebruik de nieuwe functie voor foutieve lengte
            continue

        # Controleer letters en toon resultaat
        controleer_letters(te_raden_woord, invoer, geraden_letters, geraden_letters_zonder_kleur)

        # Toon de huidige status van geraden letters
        print("Huidige voortgang: " + "".join(geraden_letters))

        # Controleer of het woord volledig geraden is
        if "".join(geraden_letters_zonder_kleur) == te_raden_woord:
            print_geraden()  # Gebruik de nieuwe functie voor correct geraden woord
            return True
        else:
            print_verkeerd_geraden()  # Gebruik de nieuwe functie voor verkeerd geraden woord
        
        pogingen += 1  # Verhoog het aantal pogingen na elke beurt

    print_helaas_geraden_woord(te_raden_woord)  # Gebruik de nieuwe functie voor wanneer het woord niet geraden is
    return False  # Als de speler het woord niet geraden heeft na 5 pogingen


def toon_te_raden_woord(speler_naam, te_raden_woord):
    """Toon het te raden woord als de speler 'Joris' heet."""
    if speler_naam.lower() == "joris":
        print(f"[DEBUG] Het te raden woord is: {te_raden_woord}")


def bingokaart():
    """Genereer een lege bingokaart."""
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
        volledig_x = True
        for vakje in rij:
            if vakje != "X":
                volledig_x = False
                break
        if volledig_x:
            return True

    # Controleer kolommen
    aantal_kolommen = len(kaart[0])
    for kolom in range(aantal_kolommen):
        volledig_x = True
        for rij in kaart:
            if rij[kolom] != "X":
                volledig_x = False
                break
        if volledig_x:
            return True

    return False


def grabbel_ballen(team, bingokaart, groene_ballen, rode_ballen):
    """Simuleer het grabbelen van ballen en print het resultaat met de juiste meervoudsvorm."""
    print(f"{team} grabbelt een bal...")
    bal = random.choice(["groen", "rood", "geel"])
    print(f"{team} trekt een {bal} bal!")

    # Variabele voor enkelvoud/meervoud
    if bal == "groen":
        groene_ballen += 1
        bal_of_ballen = "groene bal" if groene_ballen == 1 else "groene ballen"
        print(f"{team} heeft nu {groene_ballen} {bal_of_ballen}.")
        # Simuleer een willekeurige positie op de bingokaart
        rij, kolom = random.randint(0, 4), random.randint(0, 4)
        bingokaart[rij][kolom] = "X"
        print_bingokaart(bingokaart)
        return groene_ballen, rode_ballen, True
    elif bal == "rood":
        rode_ballen += 1
        bal_of_ballen = "rode bal" if rode_ballen == 1 else "rode ballen"
        print(f"{team} heeft nu {rode_ballen} {bal_of_ballen}.")
        return groene_ballen, rode_ballen, False
    else:
        print(f"{team} krijgt geen verdere actie.")
        return groene_ballen, rode_ballen, True