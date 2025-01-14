import random
from Lingo.lingowords import woordenlijst

def bingokaart():
    return [[0] * 4 for _ in range(4)]

def print_bingokaart(kaart):
    for rij in kaart:
        print(" ".join(str(getal) if getal != 0 else "_" for getal in rij))

def check_bingo(kaart):
    # Controleer rijen, kolommen en diagonalen op bingo
    for rij in kaart:
        if all(getal != 0 for getal in rij):
            return True

    for kolom in range(4):
        if all(rij[kolom] != 0 for rij in kaart):
            return True

    if all(kaart[i][i] != 0 for i in range(4)) or all(kaart[i][3 - i] != 0 for i in range(4)):
        return True

    return False

def grabbel_ballen(team, kaart, groene_ballen, rode_ballen):
    groene = ["groen", "groen", "groen"]
    rode = ["rood", "rood", "rood"]
    nummers = [n for n in range(1, 17)]
    ballenbak = groene + rode + nummers

    print(f"{team} mag twee keer grabbelen!")
    doorgaan = True

    for _ in range(2):
        if not doorgaan:
            break
        bal = random.choice(ballenbak)
        ballenbak.remove(bal)

        if bal == "groen":
            print(f"{team} heeft een groene bal getrokken!")
            groene_ballen += 1
        elif bal == "rood":
            print(f"{team} heeft een rode bal getrokken!")
            rode_ballen += 1
            doorgaan = False
        else:
            print(f"{team} heeft balnummer {bal} getrokken!")
            rijnummer, kolomnummer = divmod(bal - 1, 4)
            kaart[rijnummer][kolomnummer] = bal

    print(f"Bingo-kaart van {team}:")
    print_bingokaart(kaart)
    return groene_ballen, rode_ballen, doorgaan

def selecteer_woord_en_beginletter(woordenlijst):
    woord = random.choice(woordenlijst)
    geraden_letters = ["_"] * len(woord)
    geraden_letters[0] = woord[0]  # De eerste letter is altijd zichtbaar
    return woord, geraden_letters

def controleer_letters(te_raden_woord, invoer, geraden_letters):
    nieuwe_geraden = geraden_letters[:]
    for i, letter in enumerate(invoer):
        if te_raden_woord[i] == letter:
            nieuwe_geraden[i] = letter
        elif letter in te_raden_woord:
            if nieuwe_geraden[i] == "_":
                nieuwe_geraden[i] = "*"
    return nieuwe_geraden

def vraag_opnieuw_spelen():
    antwoord = input("Wil je opnieuw spelen? (ja/nee): ").strip().lower()
    return antwoord == "ja"