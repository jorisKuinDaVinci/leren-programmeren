import random


def kies_willekeurig_woord(woordenlijst):
    """Kies een willekeurig woord uit de woordenlijst."""
    return random.choice(woordenlijst)


def controleer_letters(te_raden_woord, invoer, geraden_letters):
    """Controleer welke letters correct zijn en vervang de underscores."""
    for i in range(len(te_raden_woord)):
        if te_raden_woord[i] == invoer[i]:
            geraden_letters[i] = invoer[i]
    return geraden_letters


def raad_woord(te_raden_woord, geraden_letters):
    """Laat de speler proberen het woord te raden."""
    pogingen = 0
    while pogingen < 5:
        print("Raad het woord: ", " ".join(geraden_letters))
        invoer = input("Jouw gok: ").lower()
        if len(invoer) != len(te_raden_woord):
            print("Fout: Het woord moet dezelfde lengte hebben als het te raden woord!")
            continue

        pogingen += 1
        geraden_letters = controleer_letters(te_raden_woord, invoer, geraden_letters)

        if "".join(geraden_letters) == te_raden_woord:
            print("Gefeliciteerd, het woord is correct!")
            return True

    return False


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
        if all(vakje == "X" for vakje in rij):
            return True

    # Controleer kolommen
    for kolom in range(len(kaart[0])):
        if all(rij[kolom] == "X" for rij in kaart):
            return True

    return False


def grabbel_ballen(team, bingokaart, groene_ballen, rode_ballen):
    """Simuleer het grabbelen van ballen."""
    print(f"{team} grabbelt een bal...")
    bal = random.choice(["groen", "rood", "geel"])
    print(f"{team} trekt een {bal} bal!")

    if bal == "groen":
        groene_ballen += 1
        print(f"{team} heeft nu {groene_ballen} groene ballen.")
        # Simuleer een willekeurige positie op de bingokaart
        rij, kolom = random.randint(0, 4), random.randint(0, 4)
        bingokaart[rij][kolom] = "X"
        print_bingokaart(bingokaart)
        return groene_ballen, rode_ballen, True
    elif bal == "rood":
        rode_ballen += 1
        print(f"{team} heeft nu {rode_ballen} rode ballen.")
        return groene_ballen, rode_ballen, False
    else:
        print(f"{team} krijgt geen verdere actie.")
        return groene_ballen, rode_ballen, True