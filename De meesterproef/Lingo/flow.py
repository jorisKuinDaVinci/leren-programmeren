from Lingo.functions import (
    bingokaart,
    check_bingo,
    grabbel_ballen,
    selecteer_woord_en_beginletter,
    raad_woord,
    vraag_opnieuw_spelen,
)
from Lingo.teksten import (
    welkom_bericht,
    team_aan_de_beurt,
    helaas,
    einde_spel
)
from Lingo.lingowords import woordenlijst

def speel_lingo():
    welkom_bericht()
    bingokaart_team1 = bingokaart()
    bingokaart_team2 = bingokaart()
    team1_score, team2_score = 0, 0
    team1_rode_ballen, team2_rode_ballen = 0, 0
    team1_groene_ballen, team2_groene_ballen = 0, 0
    team1_foute_rij, team2_foute_rij = 0, 0
    spel_aan_de_gang = True
    huidig_team = "TEAM1"

    while spel_aan_de_gang:
        te_raden_woord, geraden_letters = selecteer_woord_en_beginletter(woordenlijst)
        team_aan_de_beurt(huidig_team, te_raden_woord[0])

        woord_geraden, geraden_letters = raad_woord(te_raden_woord, geraden_letters)

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
            helaas(huidig_team, te_raden_woord)
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
            einde_spel(huidig_team)
            break

        huidig_team = "TEAM2" if huidig_team == "TEAM1" else "TEAM1"

    if vraag_opnieuw_spelen():
        speel_lingo()
    else:
        print("Bedankt voor het spelen!")

if __name__ == "__main__":
    speel_lingo()