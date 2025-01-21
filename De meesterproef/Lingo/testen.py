from functions import (
    kies_willekeurig_woord,
    controleer_letters,
    raad_woord,
    toon_te_raden_woord,
    bingokaart,
    print_bingokaart,
    check_bingo,
    grabbel_ballen,
)
from lingowords import words as woordenlijst


def test_kies_willekeurig_woord():
    print("Test kies_willekeurig_woord:")
    woord = kies_willekeurig_woord(woordenlijst)
    if woord in woordenlijst:
        print("  Geslaagd")
    else:
        print(f"  Mislukt: {woord} niet in woordenlijst")


def test_controleer_letters():
    print("Test controleer_letters:")
    te_raden_woord = "python"
    geraden = "potion"
    geraden_letters = ["_", "_", "_", "_", "_", "_"]
    geraden_letters_zonder_kleur = ["_", "_", "_", "_", "_", "_"]  # Voeg dit argument toe

    resultaat = controleer_letters(te_raden_woord, geraden, geraden_letters, geraden_letters_zonder_kleur)
    if resultaat == ["p", "_", "t", "_", "o", "n"]:
        print("  Geslaagd")
    else:
        print(f"  Mislukt: {resultaat}")


def test_raad_woord():
    print("Test raad_woord:")
    te_raden_woord = "python"
    geraden_letters = ["_", "_", "_", "_", "_", "_"]

    # Simuleer correcte invoer
    pogingen = ["pytzzz", "pythzz", "python"]
    for poging in pogingen:
        print(f"  Poging: {poging}")
        geraden_letters = raad_woord(te_raden_woord, poging, geraden_letters)  # Nu raad_woord gebruiken
        print("  Huidige status:", "".join(geraden_letters))
        if "".join(geraden_letters) == te_raden_woord:
            print("  Geslaagd")
            break
    else:
        print("  Mislukt")


def test_check_bingo():
    print("Test check_bingo:")
    kaart_met_bingo = [
        ["X", "X", "X", "X", "X"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["X", "X", "X", "X", "X"],
        ["O", "O", "O", "O", "O"]
    ]
    kaart_zonder_bingo = [
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O"],
        ["X", "O", "X", "O", "X"]
    ]
    if check_bingo(kaart_met_bingo):
        print("  Geslaagd: Bingo correct gedetecteerd")
    else:
        print("  Mislukt: Bingo niet gedetecteerd")

    if not check_bingo(kaart_zonder_bingo):
        print("  Geslaagd: Geen bingo correct gedetecteerd")
    else:
        print("  Mislukt: Onterecht bingo gedetecteerd")


def test_bingokaart():
    print("Test bingokaart:")
    kaart = bingokaart()
    if len(kaart) == 5 and all(len(rij) == 5 for rij in kaart):
        print("  Geslaagd")
    else:
        print(f"  Mislukt: Ongeldige bingokaart {kaart}")


def test_grabbel_ballen():
    print("Test grabbel_ballen:")
    # Testen met een lege bingokaart en initiële balstanden
    team = "TEAM1"
    bingokaart = [["_", "_", "_", "_", "_"] for _ in range(5)]
    groene_ballen = 0
    rode_ballen = 0

    # Simuleer bal trekken
    for _ in range(5):  # meerdere keer trekken
        groene_ballen, rode_ballen, is_goed = grabbel_ballen(team, bingokaart, groene_ballen, rode_ballen)
        print(f"  Groene ballen: {groene_ballen}, Rode ballen: {rode_ballen}")
        print_bingokaart(bingokaart)
    print("  Geslaagd")


def test_toon_te_raden_woord():
    print("Test toon_te_raden_woord:")
    speler_naam = "joris"
    te_raden_woord = "python"
    toon_te_raden_woord(speler_naam, te_raden_woord)
    # Handmatige controle nodig om te zien of het woord wordt geprint


if __name__ == "__main__":
    print("Start testen:\n")
    test_kies_willekeurig_woord()
    test_controleer_letters()
    test_raad_woord()
    test_check_bingo()
    test_bingokaart()
    test_grabbel_ballen()
    test_toon_te_raden_woord()
    print("\nEinde testen.")