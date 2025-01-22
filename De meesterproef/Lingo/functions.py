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

# Functie die het woord van de speler controleert
def raad_woord(te_raden_woord, geraden_letters):
    """
    Laat een speler een woord raden en controleer of het correct is.
    Retourneert True als het woord correct is, anders False.
    """
    pogingen = 5  # Aantal pogingen per woord
    while pogingen > 0:
        gok = input(f"Voer je woord in ({len(te_raden_woord)} letters): ").lower()
        
        # Controleer of de gok de juiste lengte heeft
        if len(gok) != len(te_raden_woord):
            print(f"Fout: het woord moet {len(te_raden_woord)} letters lang zijn.")
            continue
        
        if gok == te_raden_woord:
            print("Gefeliciteerd! Je hebt het woord geraden.")
            return True
        else:
            # Geef feedback op basis van de gekleurde letters
            print("Feedback: ", controleer_letters(gok, te_raden_woord))
            pogingen -= 1
            print(f"Niet correct, probeer het opnieuw. Pogingen over: {pogingen}")
    
    print(f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}")
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
        print(" | ".join([str(kaart[i * 5 + j]).rjust(2) for j in range(5)]))
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

# Functie die een rode, groene, blauwe of vraagteken bal trekt
def grabbel_ballen(huidig_team, bingokaart, groene_ballen, rode_ballen):
    """
    Trek een bal uit de ballenbak voor het team en verwerk de effect.
    Retourneer de bijgewerkte aantallen van groene en rode ballen.
    """
    ballenbak = ["groen", "groen", "groen", "blauw", "blauw", "blauw", "blauw", "blauw", "blauw", "blauw", "blauw", "blauw", "rood", "rood", "rood", "?"]
    gekozen_bal = random.choice(ballenbak)
    
    if gekozen_bal == "groen":
        groene_ballen += 1
        print(f"{huidig_team} heeft een groene bal! Je mag nog een bal trekken.")
    elif gekozen_bal == "rood":
        rode_ballen += 1
        print(f"{huidig_team} heeft een rode bal! De beurt gaat naar het andere team.")
    elif gekozen_bal == "blauw":
        getal = random.randint(1, 75)
        print(f"{huidig_team} heeft een blauwe bal met nummer {getal}. Dit wordt afgestreept op de bingokaart.")
        # Voer de juiste afstrepactie uit op de bingokaart hier
    elif gekozen_bal == "?":
        print(f"{huidig_team} heeft een vraagtekenbal! Kies een getal om af te strepen.")
        # Laat het team een getal kiezen
        # Voer de afstrepactie uit op de bingokaart hier

    return groene_ballen, rode_ballen, gekozen_bal