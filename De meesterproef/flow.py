import random
from functions import (
    bingokaart,
    print_bingokaart,
    check_bingo,
    grabbel_ballen,
    selecteer_woord_en_beginletter,
    controleer_letters,
    vraag_opnieuw_spelen,
)

WOORDENLIJST = ["voorbeeld", "woordenlijst", "testwoord", "spel", "lingo", "python"]

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
        te_raden_woord, geraden_letters = selecteer_woord_en_beginletter(WOORDENLIJST)
        print(f"\n{huidig_team} is aan de beurt! Het woord begint met: {te_raden_woord[0]}")
        
        woord_geraden = False
        pogingen = 0

        while pogingen < 5 and not woord_geraden:
            print("Raad het woord: ", " ".join(geraden_letters))
            invoer = input("Jouw gok: ").lower()
            if len(invoer) != len(te_raden_woord):
                print("Fout: Het woord moet dezelfde lengte hebben!")
                continue

            pogingen += 1
            geraden_letters = controleer_letters(te_raden_woord, invoer, geraden_letters)

            if "".join(geraden_letters) == te_raden_woord:
                woord_geraden = True
                print(f"Gefeliciteerd {huidig_team}, het woord was correct!")

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

        if (
            team1_groene_ballen == 3
            or check_bingo(bingokaart_team1)
            or team1_score == 10
            or team1_rode_ballen == 3
            or team1_foute_rij == 3
        ) or (
            team2_groene_ballen == 3
            or check_bingo(bingokaart_team2)
            or team2_score == 10
            or team2_rode_ballen == 3
            or team2_foute_rij == 3
        ):
            print(f"Einde spel! {huidig_team} wint!")
            break

        huidig_team = "TEAM2" if huidig_team == "TEAM1" else "TEAM1"

    if vraag_opnieuw_spelen():
        speel_lingo()
    else:
        print("Bedankt voor het spelen!")

speel_lingo()