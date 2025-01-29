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
    feedback = [""] * len(te_raden_woord)
    te_raden_lijst = list(te_raden_woord)  # Kopieer het te raden woord om verbruikte letters bij te houden

    # Eerst groene letters markeren
    for i in range(len(gok)):
        if gok[i] == te_raden_woord[i]:
            feedback[i] = colored(gok[i], "green")
            te_raden_lijst[i] = None  # Verwijder de letter zodat deze niet meer als geel telt

    # Dan gele letters markeren
    for i in range(len(gok)):
        if feedback[i] == "":  # Alleen als het nog niet groen is
            if gok[i] in te_raden_lijst:
                feedback[i] = colored(gok[i], "yellow")
                te_raden_lijst[te_raden_lijst.index(gok[i])] = None  # Zorg dat een letter maar één keer geel wordt
            else:
                feedback[i] = colored(gok[i], "red")  # Rood als het nergens voorkomt

    return " ".join(feedback)

# Functie die een willekeurig woord kiest uit de woordenlijst
def kies_willekeurig_woord(woordenlijst):
    return random.choice(woordenlijst)

def raad_woord(te_raden_woord, geraden_letters):
    pogingen = 5
    while pogingen > 0:
        poging = vraag_raad_woord(geraden_letters, te_raden_woord)

        if poging == te_raden_woord:
            toon_woord_geraden()
            return True

        for i in range(len(poging)):
            if i < len(te_raden_woord) and poging[i] == te_raden_woord[i]:
                geraden_letters[i] = poging[i]

        print(f"Hint: {''.join(geraden_letters)}")
        pogingen -= 1

    print(f"Jammer, het woord was {te_raden_woord}.")
    return False

def vraag_raad_woord(geraden_letters, te_raden_woord):
    while True:
        poging = input(f"Raad het woord: {''.join(geraden_letters)} ").lower()

        if len(poging) != len(te_raden_woord):
            print(f"Fout: Het woord moet {len(te_raden_woord)} letters lang zijn.")
            continue
        
        return poging

def bingokaart():
    kaart = random.sample(range(1, 76), 25)
    kaart[12] = "Gratis"
    return kaart

def print_bingokaart(kaart):
    for i in range(5):
        print(" | ".join([str(kaart[i * 5 + j]) for j in range(5)]))
        print("-" * 29)

def check_bingo(kaart):
    for i in range(5):
        bingo = True
        for j in range(5):
            if kaart[i * 5 + j] != 'X':
                bingo = False
                break
        if bingo:
            return True

    for j in range(5):
        bingo = True
        for i in range(5):
            if kaart[i * 5 + j] != 'X':
                bingo = False
                break
        if bingo:
            return True

    bingo = True
    for i in range(5):
        if kaart[i * 5 + i] != 'X':
            bingo = False
            break
    if bingo:
        return True

    bingo = True
    for i in range(5):
        if kaart[i * 5 + (4 - i)] != 'X':
            bingo = False
            break
    if bingo:
        return True

    return False

def grabbel_ballen(team, ballenbak, bingokaart, groene_ballen, rode_ballen):
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
    return groene_ballen, rode_ballen, gekozen_bal

def controleer_of_er_een_winnaar_is(team1_score, team2_score, team1_groene_ballen, team2_groene_ballen,
                                     team1_rode_ballen, team2_rode_ballen, team1_foute_rij, team2_foute_rij,
                                     bingokaart_team1, bingokaart_team2):
    if team1_score >= 3 or team1_groene_ballen == 3 or check_bingo(bingokaart_team1):
        team_groene_ballen_winnaar("Team 1")
        return True
    elif team2_score >= 3 or team2_groene_ballen == 3 or check_bingo(bingokaart_team2):
        team_groene_ballen_winnaar("Team 2")
        return True
    elif team1_rode_ballen == 3 or team1_foute_rij == 3:
        team_rode_ballen_verliezer("Team 1")
        return True
    elif team2_rode_ballen == 3 or team2_foute_rij == 3:
        team_rode_ballen_verliezer("Team 2")
        return True
    return False

# Functie die het te raden woord toont voor "Joris"
def toon_te_raden_woord(speler_naam, te_raden_woord):
    """Toon het te raden woord (debugfunctie)."""
    if speler_naam.lower() == "joris":
        print(f"Debug ({speler_naam}): Het te raden woord is '{te_raden_woord}'.")