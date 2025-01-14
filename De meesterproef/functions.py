import random

# Bingo-kaarten initialiseren
def init_bingokaart():
    return [["" for _ in range(4)] for _ in range(4)]

# Toon bingo-kaart
def print_bingokaart(kaart):
    for rij in kaart:
        print(" | ".join([str(item).rjust(2) if item else "  " for item in rij]))
    print()

# Controleer op bingo
def check_bingo(kaart):
    # Controleer rijen en kolommen
    for i in range(4):
        if all(kaart[i][j] != "" for j in range(4)) or all(kaart[j][i] != "" for j in range(4)):
            return True
    # Controleer diagonalen
    if all(kaart[i][i] != "" for i in range(4)) or all(kaart[i][3 - i] != "" for i in range(4)):
        return True
    return False

# Grabbelen in de ballenbak
def grabbel_ballen(huidig_team, bingokaart, groene_ballen, rode_ballen):
    BALLENBAK = ["ROOD", "ROOD", "ROOD", "GROEN", "GROEN", "GROEN"] + [i for i in range(1, 33)]
    for _ in range(2):
        bal = random.choice(BALLENBAK)
        print(f"{huidig_team} trekt bal: {bal}")
        if bal == "ROOD":
            rode_ballen += 1
            print(f"{huidig_team} heeft nu {rode_ballen} rode bal(len)!")
            return groene_ballen, rode_ballen, False
        elif bal == "GROEN":
            groene_ballen += 1
            print(f"{huidig_team} heeft nu {groene_ballen} groene bal(len)!")
        else:
            # Voeg nummer toe aan bingo-kaart
            toegevoegd = False
            for i in range(4):
                for j in range(4):
                    if bingokaart[i][j] == "":
                        bingokaart[i][j] = bal
                        toegevoegd = True
                        break
                if toegevoegd:
                    break
    return groene_ballen, rode_ballen, True