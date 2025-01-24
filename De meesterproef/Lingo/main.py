from lingowords import words as woordenlijst
from functions import (
    kies_willekeurig_woord, 
    raad_woord,
    bingokaart, 
    print_bingokaart,
    grabbel_ballen, 
    controleer_of_er_een_winnaar_is,
    toon_te_raden_woord
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

    while True:
        print("\n--- Beurt Team 1 ---")
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)
        eerste_letter = te_raden_woord[0]
        print_beurt_start("Team 1", eerste_letter)

        # Toon het te raden woord als spelernaam "Joris"
        toon_te_raden_woord(speler_naam, te_raden_woord)  # Voeg dit toe om het woord te tonen bij "Joris"

        if raad_woord(te_raden_woord, geraden_letters):
            team1_score += 1
            team1_groene_ballen, team1_rode_ballen, _ = grabbel_ballen("Team 1", ["groen", "groen", "groen", "rood", "rood", "?"], bingokaart_team1, team1_groene_ballen, team1_rode_ballen)

        print("\n--- Beurt Team 2 ---")
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)
        eerste_letter = te_raden_woord[0]
        print_beurt_start("Team 2", eerste_letter)

        # Toon het te raden woord als spelernaam "Joris"
        toon_te_raden_woord(speler_naam, te_raden_woord)  # Voeg dit toe om het woord te tonen bij "Joris"

        if raad_woord(te_raden_woord, geraden_letters):
            team2_score += 1
            team2_groene_ballen, team2_rode_ballen, _ = grabbel_ballen("Team 2", ["groen", "groen", "groen", "rood", "rood", "?"], bingokaart_team2, team2_groene_ballen, team2_rode_ballen)

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