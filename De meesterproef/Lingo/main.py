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
    vraag_naam  # voeg deze functie toe om de naam van de speler te vragen
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

    # Functie voor het spelen van de beurt van een team
    def speel_beurt(team, te_raden_woord, geraden_letters, team_score, team_groene_ballen, team_rode_ballen, bingokaart_team):
        eerste_letter = te_raden_woord[0]
        print_beurt_start(team, eerste_letter)

        # Toon het te raden woord als spelernaam "Joris"
        toon_te_raden_woord(speler_naam, te_raden_woord)

        if raad_woord(te_raden_woord, geraden_letters):
            team_score += 1
            team_groene_ballen, team_rode_ballen, _ = grabbel_ballen(team, ["groen", "groen", "groen", "rood", "rood", "?"], bingokaart_team, team_groene_ballen, team_rode_ballen)
        
        return team_score, team_groene_ballen, team_rode_ballen

    while True:
        print("\n--- Beurt Team 1 ---")
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)

        team1_score, team1_groene_ballen, team1_rode_ballen = speel_beurt(
            "Team 1", te_raden_woord, geraden_letters, team1_score, team1_groene_ballen, team1_rode_ballen, bingokaart_team1
        )

        print("\n--- Beurt Team 2 ---")
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)

        team2_score, team2_groene_ballen, team2_rode_ballen = speel_beurt(
            "Team 2", te_raden_woord, geraden_letters, team2_score, team2_groene_ballen, team2_rode_ballen, bingokaart_team2
        )

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