from functions import (
    kies_willekeurig_woord,
    raad_woord,
    toon_te_raden_woord,
    bingokaart,
    print_bingokaart,
    check_bingo,
    grabbel_ballen,
)
from teksten import (
    print_introductie,
    print_beurt_start,
    print_winnaar,
    print_afsluiting,
    vraag_opnieuw_spelen,
    vraag_naam,
    toon_woord_fout,
)
from lingowords import words as woordenlijst


# Start het spel
def speel_lingo():
    # Vraag speler naam en geef introductie
    speler_naam = vraag_naam()
    print_introductie()

    # Maak bingokaarten en initialiseerscores
    bingokaart_team1 = bingokaart()
    bingokaart_team2 = bingokaart()
    team1_score, team2_score = 0, 0
    team1_rode_ballen, team2_rode_ballen = 0, 0
    team1_groene_ballen, team2_groene_ballen = 0, 0
    team1_foute_rij, team2_foute_rij = 0, 0
    spel_aan_de_gang = True
    huidig_team = "TEAM1"

    while spel_aan_de_gang:
        # Kies een nieuw woord en initialiseert geraden letters als lijst
        te_raden_woord = kies_willekeurig_woord(woordenlijst)
        geraden_letters = ["_"] * len(te_raden_woord)  # Lijst om status bij te houden

        # Debug: Toon te raden woord
        toon_te_raden_woord(speler_naam, te_raden_woord)

        # Start de beurt en woord raden
        print_beurt_start(huidig_team, te_raden_woord[0])
        woord_geraden = raad_woord(te_raden_woord, geraden_letters)

        # Verwerk het resultaat
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

            # Controleer of de beurt direct eindigt door een rode bal
            if not doorgaan:
                print(f"{huidig_team} heeft een rode bal getrokken. De beurt eindigt.")
                huidig_team = "TEAM2" if huidig_team == "TEAM1" else "TEAM1"
                continue
        else:
            toon_woord_fout(te_raden_woord)
            if huidig_team == "TEAM1":
                team1_foute_rij += 1
            else:
                team2_foute_rij += 1

        # Toon de huidige bingo-kaarten
        print(f"De bingo-kaart van {huidig_team}:")
        print_bingokaart(bingokaart_team1 if huidig_team == "TEAM1" else bingokaart_team2)

        # Controleer op bingo voor het huidige team
        if check_bingo(bingokaart_team1 if huidig_team == "TEAM1" else bingokaart_team2):
            print(f"{huidig_team} heeft bingo!")
            print_winnaar(huidig_team)
            break

        # Controleer op andere eindcondities
        if (
            team1_groene_ballen == 3
            or team1_score == 10
            or team1_rode_ballen == 3
            or team1_foute_rij == 3
        ) or (
            team2_groene_ballen == 3
            or team2_score == 10
            or team2_rode_ballen == 3
            or team2_foute_rij == 3
        ):
            print_winnaar(huidig_team)
            break

        # Wissel van team
        huidig_team = "TEAM2" if huidig_team == "TEAM1" else "TEAM1"

    # Vraag of het spel opnieuw moet worden gespeeld
    if vraag_opnieuw_spelen():
        speel_lingo()
    else:
        print_afsluiting()


# Start het spel
speel_lingo()