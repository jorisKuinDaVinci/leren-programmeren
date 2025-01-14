import random
from functions import bingokaart, print_bingokaart, check_bingo, grabbel_ballen

# Woordenlijst
WOORDENLIJST = ["voorbeeld", "woordenlijst", "testwoord", "spel", "lingo", "python"]

# Hoofdspel
def speel_lingo():
    bingokaart_team1 = bingokaart()
    bingokaart_team2 = bingokaart()
    team1_score, team2_score = 0, 0
    team1_rode_ballen, team2_rode_ballen = 0, 0
    team1_groene_ballen, team2_groene_ballen = 0, 0
    team1_foute_rij, team2_foute_rij = 0, 0
    spel_aan_de_gang = True
    huidig_team = "TEAM1"

    while spel_aan_de_gang:
        # Selecteer een woord en beginletter
        te_raden_woord = random.choice(WOORDENLIJST)
        beginletter = te_raden_woord[0]
        geraden_letters = [beginletter] + ["_"] * (len(te_raden_woord) - 1)
        print(f"\n{huidig_team} is aan de beurt! Het woord begint met: {beginletter}")
        
        woord_geraden = False
        pogingen = 0

        # Pogingen om het woord te raden
        while pogingen < 5 and not woord_geraden:
            print("Raad het woord: ", " ".join(geraden_letters))
            invoer = input("Jouw gok: ").lower()
            if len(invoer) != len(te_raden_woord):
                print("Fout: Het woord moet dezelfde lengte hebben!")
                continue

            pogingen += 1

            # Controleer letters
            for i in range(len(te_raden_woord)):
                if invoer[i] == te_raden_woord[i]:
                    geraden_letters[i] = invoer[i]  # Juiste plaats (groen)
                elif invoer[i] in te_raden_woord:
                    print(f"Letter {invoer[i]} is in het woord, maar op de verkeerde plaats (geel).")

            if "".join(geraden_letters) == te_raden_woord:
                woord_geraden = True
                print(f"Gefeliciteerd {huidig_team}, het woord was correct!")

        # Evaluatie na pogingen
        if woord_geraden:
            if huidig_team == "TEAM1":
                team1_foute_rij = 0
                team1_score += 1
                team1_groene_ballen, team1_rode_ballen, doorgaan = grabbel_ballen(
                    huidig_team, bingokaart_team1, team1_groene_ballen, team1_rode_ballen
                )
            else:
                team2_foute_rij = 0
                team2_score += 1
                team2_groene_ballen, team2_rode_ballen, doorgaan = grabbel_ballen(
                    huidig_team, bingokaart_team2, team2_groene_ballen, team2_rode_ballen
                )
        else:
            print(f"Helaas {huidig_team}, het woord was: {te_raden_woord}")
            if huidig_team == "TEAM1":
                team1_foute_rij += 1
            else:
                team2_foute_rij += 1

        # Controleer eindvoorwaarden
        if (
            team1_groene_ballen == 3
            or check_bingo(bingokaart_team1)
            or team1_score == 10
            or team1_rode_ballen == 3
            or team1_foute_rij == 3
        ):
            print(f"Einde spel! {huidig_team} wint!")
            break
        if (
            team2_groene_ballen == 3
            or check_bingo(bingokaart_team2)
            or team2_score == 10
            or team2_rode_ballen == 3
            or team2_foute_rij == 3
        ):
            print(f"Einde spel! {huidig_team} wint!")
            break

        # Wissel team
        huidig_team = "TEAM2" if huidig_team == "TEAM1" else "TEAM1"

    # Vraag of spelers opnieuw willen spelen
    opnieuw = input("Wil je opnieuw spelen? (ja/nee): ").lower()
    if opnieuw == "ja":
        speel_lingo()
    else:
        print("Bedankt voor het spelen!")

# Start het spel
speel_lingo()