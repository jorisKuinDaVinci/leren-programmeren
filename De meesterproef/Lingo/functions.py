import random
from teksten import print_fout_woord_lengte


def kies_willekeurig_woord(woordenlijst):
    """Selecteer een willekeurig woord uit de woordenlijst."""
    return random.choice(woordenlijst)


def bingokaart():
    """Genereer een lege bingokaart van 4x4."""
    return [["_" for _ in range(4)] for _ in range(4)]


def print_bingokaart(bingokaart):
    """Print de bingokaart in een 4x4 raster."""
    for rij in bingokaart:
        print(" ".join(rij))


def check_bingo(bingokaart):
    """Controleer of er een bingo is (horizontaal, verticaal of diagonaal)."""
    # Controleer horizontale en verticale lijnen
    for i in range(4):
        if all(vakje == "X" for vakje in bingokaart[i]) or all(
            bingokaart[j][i] == "X" for j in range(4)
        ):
            return True
    # Controleer diagonalen
    if all(bingokaart[i][i] == "X" for i in range(4)) or all(
        bingokaart[i][3 - i] == "X" for i in range(4)
    ):
        return True
    return False


def grabbel_ballen(huidig_team, bingokaart, groene_ballen, rode_ballen):
    """Laat een team ballen grabbelen en verwerk de resultaten."""
    print(f"{huidig_team} mag in de ballenbak grabbelen!")
    doorgaan = True
    for _ in range(2):
        bal = random.choice(["groen", "rood", "nummer"])
        if bal == "groen":
            groene_ballen += 1
            print(f"{huidig_team} trok een groene bal!")
        elif bal == "rood":
            rode_ballen += 1
            print(f"{huidig_team} trok een rode bal!")
            doorgaan = False
            break
        else:
            x, y = random.randint(0, 3), random.randint(0, 3)
            bingokaart[x][y] = "X"
            print(f"{huidig_team} markeerde vakje ({x + 1}, {y + 1}) op de bingokaart.")
    print_bingokaart(bingokaart)
    return groene_ballen, rode_ballen, doorgaan


def controleer_letters(te_raden_woord, invoer, geraden_letters):
    """Controleer de ingevoerde letters en update geraden letters."""
    nieuwe_geraden_letters = geraden_letters[:]
    for i in range(len(te_raden_woord)):
        if invoer[i] == te_raden_woord[i]:
            nieuwe_geraden_letters[i] = invoer[i]
        elif invoer[i] in te_raden_woord and nieuwe_geraden_letters[i] == "_":
            print(f"De letter {invoer[i]} zit in het woord, maar op een andere plek.")
    return nieuwe_geraden_letters


def raad_woord(te_raden_woord, geraden_letters):
    """Laat een team het woord raden en controleer de pogingen."""
    pogingen = 0
    while pogingen < 5:
        print("Raad het woord: ", " ".join(geraden_letters))
        invoer = input("Jouw gok: ").lower()
        if len(invoer) != len(te_raden_woord):
            print_fout_woord_lengte()
            continue
        pogingen += 1
        geraden_letters = controleer_letters(te_raden_woord, invoer, geraden_letters)
        if "".join(geraden_letters) == te_raden_woord:
            print("Gefeliciteerd, je hebt het woord geraden!")
            return True
    return False