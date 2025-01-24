import random
from termcolor import colored

# Functie die het woord van de speler vergelijkt met het te raden woord en gekleurde feedback geeft
def controleer_letters(gok, te_raden_woord):
    """
    Vergelijk de ingevoerde gok met het te raden woord en geef gekleurde feedback:
    Groen (correcte letter op de juiste plaats),
    Geel (correcte letter op de verkeerde plaats),
    Rood (foutieve letter).
    """
    feedback = []
    for i in range(len(te_raden_woord)):
        if gok[i] == te_raden_woord[i]:
            # Groen voor de correcte letter op de juiste positie
            feedback.append(colored(gok[i], "green"))
        elif gok[i] in te_raden_woord:
            # Geel voor correcte letter op verkeerde positie
            feedback.append(colored(gok[i], "yellow"))
        else:
            # Rood voor foutieve letter
            feedback.append(colored(gok[i], "red"))
    
    # De feedback als een string teruggeven
    return " ".join(feedback)

# Functie die een willekeurig woord kiest uit de woordenlijst
def kies_willekeurig_woord(woordenlijst):
    """
    Kies een willekeurig woord uit de gegeven lijst.
    """
    return random.choice(woordenlijst)

def raad_woord(te_raden_woord, geraden_letters):
    """Laat een team een woord raden en controleer de hint."""
    pogingen = 5
    while pogingen > 0:
        poging = input(f"Raad het woord: {''.join(geraden_letters)} ").lower()

        if poging == te_raden_woord:
            print("Correct! Het woord is geraden.")
            return True

        # Toon hints en vul goed geraden letters in
        for i in range(len(poging)):
            if i < len(te_raden_woord) and poging[i] == te_raden_woord[i]:
                geraden_letters[i] = poging[i]

        print(f"Hint: {''.join(geraden_letters)}")
        pogingen -= 1

    print(f"Jammer, het woord was {te_raden_woord}.")
    return False

def toon_te_raden_woord(speler_naam, te_raden_woord):
    """Toon het te raden woord (debugfunctie)."""
    if speler_naam.lower() == "joris":
        print(f"Debug ({speler_naam}): Het te raden woord is '{te_raden_woord}'.")

# Functie die de bingokaart maakt
def bingokaart():
    """
    Genereer een bingokaart met 25 unieke nummers van 1 tot 75.
    Het midden van de kaart is een gratis vak.
    """
    kaart = random.sample(range(1, 76), 25)
    kaart[12] = "Gratis"  # Het middenvak is altijd gratis
    return kaart

# Functie die de bingo-kaart afdrukt
def print_bingokaart(kaart):
    """
    Print de bingo-kaart met 5 rijen van 5 kolommen.
    """
    for i in range(5):
        print(" | ".join([str(kaart[i * 5 + j]) for j in range(5)]))
        print("-" * 29)

def check_bingo(kaart):
    """
    Controleer of er een bingo is (een volledige rij, kolom of diagonaal).
    Retourneert True als er bingo is, anders False.
    """

    # Controleer horizontale rijen
    for i in range(5):
        bingo = True
        for j in range(5):
            if kaart[i * 5 + j] != 'X':  # Als een vakje niet is afgestreept
                bingo = False
                break
        if bingo:
            return True

    # Controleer verticale kolommen
    for j in range(5):
        bingo = True
        for i in range(5):
            if kaart[i * 5 + j] != 'X':  # Als een vakje niet is afgestreept
                bingo = False
                break
        if bingo:
            return True

    # Controleer de twee diagonalen
    # Van linksboven naar rechtsonder
    bingo = True
    for i in range(5):
        if kaart[i * 5 + i] != 'X':
            bingo = False
            break
    if bingo:
        return True

    # Van rechtsboven naar linksonder
    bingo = True
    for i in range(5):
        if kaart[i * 5 + (4 - i)] != 'X':
            bingo = False
            break
    if bingo:
        return True

    return False

def grabbel_ballen(team, ballenbak, bingokaart, groene_ballen, rode_ballen):
    """Laat een team grabbelen in de ballenbak."""
    if not ballenbak:
        print("De ballenbak is leeg!")
        return groene_ballen, rode_ballen, "geen"

    # Willekeurig een bal trekken
    gekozen_bal = random.choice(ballenbak)
    ballenbak.remove(gekozen_bal)

    if gekozen_bal == "groen":
        print(f"{team} trekt een GROENE bal! Extra beurt!")
        groene_ballen += 1
        return grabbel_ballen(team, ballenbak, bingokaart, groene_ballen, rode_ballen)
    elif gekozen_bal == "rood":
        print(f"{team} trekt een RODE bal! De beurt eindigt.")
        rode_ballen += 1
    elif gekozen_bal == "?":
        print(f"{team} trekt een VRAAGTEKEN! Kies een getal van de bingo-kaart om af te strepen.")
        # Laat de speler een getal kiezen
        geldig = False
        while not geldig:
            keuze = int(input(f"Welke getal wil je afstrepen? {bingokaart}: "))
            if keuze in bingokaart:
                geldig = True
                bingokaart.remove(keuze)
            else:
                print("Ongeldige keuze, probeer opnieuw.")
    else:
        print(f"{team} trekt een BAL met het nummer {gekozen_bal}. Het getal wordt afgestreept.")
        if gekozen_bal in bingokaart:
            bingokaart.remove(gekozen_bal)

    return groene_ballen, rode_ballen, gekozen_bal


def controleer_of_er_een_winnaar_is(
    team1_score, team2_score,
    team1_groene_ballen, team2_groene_ballen,
    team1_rode_ballen, team2_rode_ballen,
    team1_foute_rij, team2_foute_rij,
    bingokaart_team1, bingokaart_team2
):
    """Controleer of er een winnaar is"""
    if team1_groene_ballen == 3:
        print("Team 1 heeft 3 groene ballen! Ze winnen!")
        return True
    if team2_groene_ballen == 3:
        print("Team 2 heeft 3 groene ballen! Ze winnen!")
        return True
    if team1_score >= 10:
        print("Team 1 heeft 10 woorden geraden! Ze winnen!")
        return True
    if team2_score >= 10:
        print("Team 2 heeft 10 woorden geraden! Ze winnen!")
        return True
    if check_bingo(bingokaart_team1):
        print("Team 1 heeft bingo! Ze winnen!")
        return True
    if check_bingo(bingokaart_team2):
        print("Team 2 heeft bingo! Ze winnen!")
        return True
    if team1_rode_ballen == 3:
        print("Team 1 heeft 3 rode ballen! Ze verliezen!")
        return True
    if team2_rode_ballen == 3:
        print("Team 2 heeft 3 rode ballen! Ze verliezen!")
        return True
    if team1_foute_rij == 3:
        print("Team 1 heeft 3 foutieve rijen! Ze verliezen!")
        return True
    if team2_foute_rij == 3:
        print("Team 2 heeft 3 foutieve rijen! Ze verliezen!")
        return True

    return False