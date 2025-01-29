# de code werkt.
import random
from lingowords import words as woordenlijst
from functions import (
    kies_willekeurig_woord,
    raad_woord,
    bingokaart,
    print_bingokaart,
    grabbel_ballen,
    controleer_of_er_een_winnaar_is,
    toon_te_raden_woord,
    controleer_letters
)
from teksten import (
    print_introductie,
    print_beurt_start,
    print_afsluiting,
    vraag_naam  # Voeg deze functie toe om de naam van de speler te vragen
)

def speel_lingo():
    # Vraag de naam van de speler
    speler_naam = vraag_naam()

    print_introductie()

    # Beginwaarden voor de scores en ballen
    team1_score = 0
    team2_score = 0
    team1_groene_ballen = 0
    team2_groene_ballen = 0
    team1_rode_ballen = 0
    team2_rode_ballen = 0
    team1_foute_rij = 0
    team2_foute_rij = 0
    bingokaart_team1 = bingokaart()
    bingokaart_team2 = bingokaart()

    print("Bingo Kaart Team 1:")
    print_bingokaart(bingokaart_team1)
    print("Bingo Kaart Team 2:")
    print_bingokaart(bingokaart_team2)

    def speel_beurt(team, speler_naam, bingokaart_team, team_score, team_groene_ballen, team_rode_ballen):
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)

        eerste_letter = te_raden_woord[0]
        print_beurt_start(team, eerste_letter)

        # Toon het te raden woord alleen voor "Joris"
        if speler_naam.lower() == "joris":
            toon_te_raden_woord(speler_naam, te_raden_woord)

        # Raad het woord
        if raad_woord(te_raden_woord, geraden_letters):
            team_score += 1
            team_groene_ballen, team_rode_ballen, _ = grabbel_ballen(team, random.sample(["groen", "groen", "groen", "rood", "rood", "?"], 6), bingokaart_team, team_groene_ballen, team_rode_ballen)

        return team_score, team_groene_ballen, team_rode_ballen

    while True:
        print("\n--- Beurt Team 1 ---")
        team1_score, team1_groene_ballen, team1_rode_ballen = speel_beurt(
            "Team 1", speler_naam, bingokaart_team1, team1_score, team1_groene_ballen, team1_rode_ballen
        )

        print("\n--- Beurt Team 2 ---")
        team2_score, team2_groene_ballen, team2_rode_ballen = speel_beurt(
            "Team 2", speler_naam, bingokaart_team2, team2_score, team2_groene_ballen, team2_rode_ballen
        )

        # Controleer of er een winnaar is
        if controleer_of_er_een_winnaar_is(
            team1_score, team2_score,
            team1_groene_ballen, team2_groene_ballen,
            team1_rode_ballen, team2_rode_ballen,
            team1_foute_rij, team2_foute_rij,
            bingokaart_team1, bingokaart_team2
        ):
            break

    print_afsluiting()

# Start het spel
speel_lingo()