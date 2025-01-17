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
    """
    Laat de speler een woord raden en geef terug of het woord correct is.
    """
    while "_" in geraden_letters:
        invoer = input("Raad een woord: ")
        if len(invoer) != len(te_raden_woord):
            print(f"Je invoer moet {len(te_raden_woord)} letters lang zijn.")
            continue

        geraden_letters = controleer_letters(te_raden_woord, invoer, geraden_letters)
        print("Huidige status:", "".join(geraden_letters))

        if "".join(geraden_letters) == te_raden_woord:
            print("Gefeliciteerd! Je hebt het woord geraden!")
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