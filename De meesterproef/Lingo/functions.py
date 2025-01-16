import random
from teksten import (
    groene_bal_getrokken,
    rode_bal_getrokken,
    nummer_getrokken,
    toon_bingokaart
)
from lingowords import woordenlijst

def bingokaart():
    return [[0] * 4 for _ in range(4)]

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

    doorgaan = True

    for _ in range(2):
        if not doorgaan:
            break
        bal = random.choice(ballenbak)
        ballenbak.remove(bal)

        if bal == "groen":
            groene_bal_getrokken(team)
            groene_ballen += 1
        elif bal == "rood":
            rode_bal_getrokken(team)
            rode_ballen += 1
            doorgaan = False
        else:
            nummer_getrokken(team, bal)
            # Bereken rij- en kolomindex
            rijnummer = (bal - 1) // 4
            kolomnummer = (bal - 1) % 4
            kaart[rijnummer][kolomnummer] = bal

    toon_bingokaart(team, kaart)
    return groene_ballen, rode_ballen, doorgaan

def selecteer_woord_en_beginletter(woordenlijst):
    woord = random.choice(woordenlijst)
    geraden_letters = ["_"] * len(woord)
    geraden_letters[0] = woord[0]  # De eerste letter is altijd zichtbaar
    return woord, geraden_letters

def controleer_letters(te_raden_woord, invoer, geraden_letters):
    nieuwe_geraden = geraden_letters[:]
    for i in range(len(invoer)):
        letter = invoer[i]
        if te_raden_woord[i] == letter:
            nieuwe_geraden[i] = letter
        elif letter in te_raden_woord:
            if nieuwe_geraden[i] == "_":
                nieuwe_geraden[i] = "*"
    return nieuwe_geraden

def raad_woord(te_raden_woord, geraden_letters):
    from Lingo.teksten import raad_woord_prompt, foutieve_lengte, gefeliciteerd

    woord_geraden = False
    pogingen = 0

    while pogingen < 5 and not woord_geraden:
        invoer = raad_woord_prompt(geraden_letters)

        if len(invoer) != len(te_raden_woord):
            foutieve_lengte()
            continue

        pogingen += 1
        geraden_letters = controleer_letters(te_raden_woord, invoer, geraden_letters)

        if "".join(geraden_letters) == te_raden_woord:
            woord_geraden = True
            gefeliciteerd("")

    return woord_geraden, geraden_letters