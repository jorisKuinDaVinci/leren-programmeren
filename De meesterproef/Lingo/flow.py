import random
from functions import (
    bingokaart,
    print_bingokaart,
    check_bingo,
    grabbel_ballen,
    kies_willekeurig_woord,
    controleer_letters,
    raad_woord
)
from teksten import (
    print_introductie,
    print_beurt_start,
    print_fout_woord_lengte,
    print_winnaar,
    print_afsluiting,
    vraag_opnieuw_spelen,
    vraag_naam
)
from lingowords import words as woordenlijst


def speel_lingo():
    speler_naam = vraag_naam()

    bingokaart_team1 = bingokaart()
    bingokaart_team2 = bingokaart()
    team1_score, team2_score = 0, 0
    team1_rode_ballen, team2_rode_ballen = 0, 0
    team1_groene_ballen, team2_groene_ballen = 0, 0
    team1_foute_rij, team2_foute_rij = 0, 0
    huidig_team = "TEAM1"

    print_introductie()

    while True:
        # Selecteer een nieuw woord en start de beurt
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)
        print_beurt_start(huidig_team, te_raden_woord[0])

        # Laat het te raden woord zien als de speler Joris heet
        if speler_naam.lower() == "joris":
            print(f"[DEBUG] Het te raden woord is: {te_raden_woord}")

        # Woord raden
        woord_geraden = raad_woord(te_raden_woord, geraden_letters)

        # Resultaat verwerken
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

        # Controleer op spelwinst of verlies
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
            print_winnaar(huidig_team)
            break

        # Wissel van team
        huidig_team = "TEAM2" if huidig_team == "TEAM1" else "TEAM1"

    if vraag_opnieuw_spelen():
        speel_lingo()
    else:
        print_afsluiting()


speel_lingo()