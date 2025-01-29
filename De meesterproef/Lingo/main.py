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
    vraag_naam,
    vraag_opnieuw_spelen
)

def speel_lingo():
    # Vraag de naam van de speler en van de tweede speler
    speler_naam = vraag_naam()
    tweede_speler_naam = input("Wat is de naam van de tweede speler? ").strip()

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
    team1_geraden_woorden = 0
    team2_geraden_woorden = 0
    bingokaart_team1 = bingokaart()
    bingokaart_team2 = bingokaart()

    print("Bingo Kaart Team 1:")
    print_bingokaart(bingokaart_team1)
    print("Bingo Kaart Team 2:")
    print_bingokaart(bingokaart_team2)

    pogingen = 5  # Aantal pogingen per beurt

    def speel_beurt(team_naam, bingokaart_team, team_score, team_groene_ballen, team_rode_ballen, team_foute_rij,
                    team_geraden_woorden, pogingen):
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)
        eerste_letter = te_raden_woord[0]
        print_beurt_start(team_naam, eerste_letter)

        # Toon het te raden woord alleen voor "Joris" (als speler_naam of tweede_speler_naam gelijk is aan "Joris")
        if speler_naam.lower() == "joris" or tweede_speler_naam.lower() == "joris":
            toon_te_raden_woord(speler_naam, te_raden_woord)

        # Raad het woord
        if raad_woord(te_raden_woord, geraden_letters):
            team_score += 1
            team_geraden_woorden += 1
            team_groene_ballen, team_rode_ballen, _ = grabbel_ballen(
                team_naam, random.sample(["groen", "groen", "groen", "rood", "rood", "?"], 6), bingokaart_team, team_groene_ballen, team_rode_ballen
            )
        else:
            team_foute_rij += 1
        
        pogingen -= 1
        print(f"Nog {pogingen} pogingen over voor {team_naam}.")

        return team_score, team_groene_ballen, team_rode_ballen, team_foute_rij, team_geraden_woorden, pogingen

    while True:
        # Start de beurt voor Team 1 (speler_naam)
        print(f"\n--- Beurt {speler_naam} (Team 1) ---")
        team1_score, team1_groene_ballen, team1_rode_ballen, team1_foute_rij, team1_geraden_woorden, pogingen = speel_beurt(
            speler_naam, bingokaart_team1, team1_score, team1_groene_ballen, team1_rode_ballen, team1_foute_rij, team1_geraden_woorden, pogingen
        )

        # Start de beurt voor Team 2 (tweede_speler_naam)
        print(f"\n--- Beurt {tweede_speler_naam} (Team 2) ---")
        team2_score, team2_groene_ballen, team2_rode_ballen, team2_foute_rij, team2_geraden_woorden, pogingen = speel_beurt(
            tweede_speler_naam, bingokaart_team2, team2_score, team2_groene_ballen, team2_rode_ballen, team2_foute_rij, team2_geraden_woorden, pogingen
        )

        # Controleer of er een winnaar is
        if controleer_of_er_een_winnaar_is(
            team1_score, team2_score,
            team1_groene_ballen, team2_groene_ballen,
            team1_rode_ballen, team2_rode_ballen,
            team1_foute_rij, team2_foute_rij,
            bingokaart_team1, bingokaart_team2,
            team1_geraden_woorden, team2_geraden_woorden
        ):
            break

        # Vraag of de speler opnieuw wil spelen
        if not vraag_opnieuw_spelen():
            break

    print_afsluiting()

# Start het spel
speel_lingo()