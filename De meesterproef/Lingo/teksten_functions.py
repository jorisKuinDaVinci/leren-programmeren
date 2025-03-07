def print_introductie():
    print("Welkom bij het Lingo spel! Je zult een woord moeten raden.")
    print("Het team krijgt 5 pogingen om het woord te raden.")
    print("Groene letters staan goed, gele letters staan wel in het woord maar op de verkeerde plaats.\n")

def print_beurt_start(team, eerste_letter):
    print(f"\n{team} is aan de beurt!")
    print(f"Het te raden woord begint met: {eerste_letter}\n")

def print_winnaar(team):
    print(f"\nGefeliciteerd! {team} heeft gewonnen!")

def print_afsluiting():
    print("\nHet spel is afgelopen. Bedankt voor het spelen van Lingo!")

def vraag_opnieuw_spelen():
    antwoord = input("\nWil je opnieuw spelen? (ja/nee): ").strip().lower()
    return antwoord == "ja"

def vraag_naam():
    naam = input("Wat is je naam? ").strip()
    return naam

def print_ballenbak_leeg():
    print("De ballenbak is leeg!")

def toon_woord_geraden():
    print("Gefeliciteerd! Je hebt het woord geraden.")

def toon_woord_verkeerd():
    print("Niet correct, probeer het opnieuw.")

def print_ongeldige_keuze():
    print("Ongeldige keuze, probeer het opnieuw.")

def toon_woord_fout(te_raden_woord):
    print(f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}")

def toon_fout_woord_lengte(len_woord):
    print(f"Fout: het woord moet {len_woord} letters lang zijn.")

def team_groene_ballen_winnaar(team):
    print(f"{team} heeft 3 groene ballen! Ze winnen!")

def team_score_winnaar(team, score):
    print(f"{team} heeft {score} woorden geraden! Ze winnen!")

def team_bingo_winnaar(team):
    print(f"{team} heeft bingo! Ze winnen!")

def team_rode_ballen_verliezer(team):
    print(f"{team} heeft 3 rode ballen! Ze verliezen!")

def team_foute_rij_verliezer(team):
    print(f"{team} heeft 3 foutieve rijen! Ze verliezen!")