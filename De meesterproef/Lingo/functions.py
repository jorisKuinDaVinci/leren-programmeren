import random
from termcolor import colored
from teksten import (
    print_ballenbak_leeg,
    toon_woord_geraden,
    team_groene_ballen_winnaar,
    team_rode_ballen_verliezer
)

def controleer_letters(gok, te_raden_woord):
    """
    Vergelijkt de gok met het te raden woord en geeft gekleurde feedback.
    
    - Groen: juiste letter op de juiste plek
    - Geel: juiste letter op de verkeerde plek
    - Rood: letter komt niet voor in het woord
    """
    if len(gok) != len(te_raden_woord):
        raise ValueError("De lengte van de gok komt niet overeen met de lengte van het te raden woord.")

    feedback = [""] * len(te_raden_woord)
    te_raden_lijst = list(te_raden_woord)  # Kopieer het te raden woord om verbruikte letters bij te houden

    # Eerst groene letters markeren
    for i in range(len(gok)):
        if gok[i] == te_raden_woord[i]:
            feedback[i] = colored(gok[i], "green")  # Groene letters staan goed
            te_raden_lijst[i] = None  # Verwijder de letter zodat deze niet meer als geel telt

    # Dan gele letters markeren
    for i in range(len(gok)):
        if feedback[i] == "":  # Alleen als het nog niet groen is
            if gok[i] in te_raden_lijst:
                feedback[i] = colored(gok[i], "yellow")  # Gele letters staan wel in het woord maar op de verkeerde plek
                te_raden_lijst[te_raden_lijst.index(gok[i])] = None  # Zorg dat een letter maar één keer geel wordt
            else:
                feedback[i] = colored(gok[i], "red")  # Rood als het nergens voorkomt

    return " ".join(feedback)

def kies_willekeurig_woord(woordenlijst):
    """
    Kies een willekeurig woord uit de woordenlijst, controleer of de lijst niet leeg is.
    """
    if not woordenlijst:
        raise ValueError("De woordenlijst is leeg.")
    return random.choice(woordenlijst)

def raad_woord(te_raden_woord, geraden_letters):
    """
    Laat de speler een poging doen om het te raden woord te raden.
    """
    pogingen = 5
    while pogingen > 0:
        poging = vraag_raad_woord(geraden_letters, te_raden_woord)

        if poging == te_raden_woord:
            toon_woord_geraden()
            return True

        for i in range(len(poging)):
            if i < len(te_raden_woord) and poging[i] == te_raden_woord[i]:
                geraden_letters[i] = poging[i]

        print("Feedback:", controleer_letters(poging, te_raden_woord))
        pogingen -= 1

    print(f"Jammer, het woord was {te_raden_woord}.")
    return False

def vraag_raad_woord(geraden_letters, te_raden_woord):
    """
    Vraag de speler om een woord in te vullen en controleer de lengte.
    """
    while True:
        poging = input(f"Raad het woord: {''.join(geraden_letters)} ").lower()

        if len(poging) != len(te_raden_woord):
            print(f"Fout: Het woord moet {len(te_raden_woord)} letters lang zijn.")
            continue
        
        return poging

def bingokaart():
    """
    Genereer een bingokaart met 25 nummers, waarbij het midden een 'Gratis' vakje is.
    """
    kaart = random.sample(range(1, 76), 25)
    kaart[12] = "Gratis"  # Het middenvak is altijd 'Gratis'
    return kaart

def print_bingokaart(kaart):
    """
    Print de bingokaart.
    """
    for i in range(5):
        print(" | ".join([str(kaart[i * 5 + j]) for j in range(5)]))
        print("-" * 29)

def check_bingo(kaart):
    """
    Controleer of er bingo is (horizontaal, verticaal, diagonaal).
    """
    # Controleer horizontale lijnen
    for i in range(5):
        if all(kaart[i * 5 + j] == 'X' for j in range(5)):
            return True

    # Controleer verticale lijnen
    for j in range(5):
        if all(kaart[i * 5 + j] == 'X' for i in range(5)):
            return True

    # Controleer diagonalen
    if all(kaart[i * 5 + i] == 'X' for i in range(5)):
        return True
    if all(kaart[i * 5 + (4 - i)] == 'X' for i in range(5)):
        return True

    return False

def grabbel_ballen(team, ballenbak, bingokaart, groene_ballen, rode_ballen):
    """
    Trek een bal uit de ballenbak en pas de scores en ballen aan.
    Bij het trekken van een vraagteken bal, mag het team een keuze maken.
    """
    if not ballenbak:
        print_ballenbak_leeg()
        return groene_ballen, rode_ballen, "geen"

    gekozen_bal = random.choice(ballenbak)
    ballenbak.remove(gekozen_bal)

    if gekozen_bal == "groen":
        print(f"{team} trekt een GROENE bal! Extra beurt!")
        groene_ballen += 1
        return grabbel_ballen(team, ballenbak, bingokaart, groene_ballen, rode_ballen)
    elif gekozen_bal == "rood":
        print(f"{team} trekt een RODE bal! Ze verliezen een punt!")
        rode_ballen += 1
    elif gekozen_bal == "?":
        print(f"{team} trekt een vraagteken bal! Ze mogen kiezen.")
        
        # Vraag wat de speler wil doen bij een vraagteken bal
        keuze = input(f"{team}, kies wat je wilt doen: (1) Extra beurt of (2) Verlies een punt: ")
        
        if keuze == "1":
            print(f"{team} heeft gekozen voor een extra beurt!")
            groene_ballen += 1
        elif keuze == "2":
            print(f"{team} heeft gekozen om een punt te verliezen.")
            rode_ballen += 1
        else:
            print(f"{team} maakte een ongeldige keuze, dus ze verliezen een punt.")
            rode_ballen += 1
    return groene_ballen, rode_ballen, gekozen_bal

def controleer_of_er_een_winnaar_is(team1_score, team2_score, team1_groene_ballen, team2_groene_ballen,
                                     team1_rode_ballen, team2_rode_ballen, team1_foute_rij, team2_foute_rij,
                                     bingokaart_team1, bingokaart_team2, team1_geraden_woorden, team2_geraden_woorden):
    """
    Controleer of er een winnaar of verliezer is op basis van de voorwaarden.
    """
    # Wincondities
    if team1_groene_ballen == 3 or check_bingo(bingokaart_team1) or team1_geraden_woorden >= 10:
        team_groene_ballen_winnaar("Team 1")
        return True
    elif team2_groene_ballen == 3 or check_bingo(bingokaart_team2) or team2_geraden_woorden >= 10:
        team_groene_ballen_winnaar("Team 2")
        return True

    # Verliescondities
    if team1_rode_ballen == 3 or team1_foute_rij == 3:
        team_rode_ballen_verliezer("Team 1")
        return True
    elif team2_rode_ballen == 3 or team2_foute_rij == 3:
        team_rode_ballen_verliezer("Team 2")
        return True

    return False

def toon_te_raden_woord(speler_naam, te_raden_woord):
    """Toon het te raden woord voor debugdoeleinden (alleen voor speler 'Joris')."""
    if speler_naam.lower() == "joris":
        print(f"Debug ({speler_naam}): Het te raden woord is '{te_raden_woord}'.")