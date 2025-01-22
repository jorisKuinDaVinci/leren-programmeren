import random
from termcolor import colored

def kies_willekeurig_woord(woordenlijst):
    """Kies willekeurig een woord uit de woordenlijst."""
    return woordenlijst[random.randint(0, len(woordenlijst) - 1)]

def raad_woord(te_raden_woord, geraden_letters):
    """
    Laat een speler een woord raden en controleer of het correct is.
    Retourneert True als het woord correct is, anders False.
    """
    pogingen = 5
    while pogingen > 0:
        gok = input(f"Voer je woord in ({len(te_raden_woord)} letters): ").lower()
        if len(gok) != len(te_raden_woord):
            print(f"Fout: het woord moet {len(te_raden_woord)} letters lang zijn.")
            continue
        if gok == te_raden_woord:
            print("Gefeliciteerd! Je hebt het woord geraden.")
            return True
        else:
            pogingen -= 1
            print(f"Niet correct, probeer het opnieuw. Pogingen over: {pogingen}")
    print(f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}")
    return False

def toon_te_raden_woord(speler_naam, te_raden_woord):
    """Toon het te raden woord (debugfunctie)."""
    print(f"Debug ({speler_naam}): Het te raden woord is '{te_raden_woord}'.")

def bingokaart():
    """Genereer een bingokaart met unieke nummers van 1 t/m 18."""
    kaart = []
    while len(kaart) < 6:
        nummer = random.randint(1, 18)
        if nummer not in kaart:
            kaart.append(nummer)
    return kaart

def print_bingokaart(kaart):
    """Print de huidige status van de bingokaart."""
    kaart_copy = kaart[:]
    kaart_copy.sort()  # Handmatige sortering zonder `sorted`
    for i in range(len(kaart_copy)):
        if i > 0:
            print(", ", end="")
        print(kaart_copy[i], end="")
    print()

def check_bingo(kaart):
    """Controleer of de bingokaart leeg is."""
    return len(kaart) == 0

# Nieuwe functies voor de verwerking van ballen
def verwerk_groene_bal(huidig_team, groene_ballen):
    """Verwerk een groene bal."""
    groene_ballen += 1
    print(f"{huidig_team} heeft een groene bal! Je mag nog een keer grabbelen.")
    return groene_ballen, True  # Team mag doorgaan

def verwerk_blauwe_bal(huidig_team, bingokaart, balnummer):
    """Verwerk een blauwe bal."""
    print(f"{huidig_team} heeft een blauwe bal met nummer {balnummer}!")
    if balnummer in bingokaart:
        bingokaart.remove(balnummer)
        print(f"Nummer {balnummer} is afgestreept van de bingokaart.")
    else:
        print(f"Nummer {balnummer} stond niet op de bingokaart.")
    return bingokaart, True  # Team mag doorgaan

def verwerk_rode_bal(huidig_team, rode_ballen):
    """Verwerk een rode bal."""
    rode_ballen += 1
    print(f"{huidig_team} heeft een rode bal! De beurt gaat naar het andere team.")
    return rode_ballen, False  # Team mag niet doorgaan

def verwerk_vraagteken_bal(huidig_team, bingokaart):
    """Verwerk het vraagteken."""
    print(f"{huidig_team} heeft het vraagteken getrokken!")
    print("Je mag een willekeurig nummer op de bingokaart kiezen om af te strepen.")
    print(f"De huidige bingokaart: {bingokaart}")
    keuze = None
    while keuze not in bingokaart:
        try:
            keuze = int(input(f"Kies een nummer dat je wilt afstrepen (uit {bingokaart}): "))
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")
    bingokaart.remove(keuze)
    print(f"Nummer {keuze} is afgestreept van de bingokaart.")
    return bingokaart, True  # Team mag doorgaan

def grabbel_ballen(huidig_team, bingokaart, groene_ballen, rode_ballen):
    """
    Laat een team een bal grabbelen en verwerk het resultaat.
    - Groene bal: +1 groene bal, team mag opnieuw grabbelen.
    - Blauwe bal: cijfer wordt afgestreept van de bingokaart.
    - Rode bal: beurt gaat naar ander team.
    - Vraagteken: speler kiest een getal om af te strepen.
    """
    ballenbak = (
        [i for i in range(1, 19)]  # 18 blauwe ballen (inclusief vraagtekenbal)
        + ["vraagteken"]
        + ["groen"] * 3
        + ["rood"] * 3
    )

    random.shuffle(ballenbak)
    getrokken_bal = ballenbak[random.randint(0, len(ballenbak) - 1)]

    print(f"{huidig_team} heeft een bal getrokken: {getrokken_bal}")

    if getrokken_bal == "groen":
        groene_ballen, doorgaan = verwerk_groene_bal(huidig_team, groene_ballen)
    elif getrokken_bal == "rood":
        rode_ballen, doorgaan = verwerk_rode_bal(huidig_team, rode_ballen)
    elif getrokken_bal == "vraagteken":
        bingokaart, doorgaan = verwerk_vraagteken_bal(huidig_team, bingokaart)
    else:  # Blauwe bal
        bingokaart, doorgaan = verwerk_blauwe_bal(huidig_team, bingokaart, getrokken_bal)

    return groene_ballen, rode_ballen, doorgaan