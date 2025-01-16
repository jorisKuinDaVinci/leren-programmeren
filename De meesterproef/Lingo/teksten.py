def welkom_bericht():
    print("Welkom bij Lingo! Het leukste spel met woorden en bingo.")

def team_aan_de_beurt(team, beginletter):
    print(f"\n{team} is aan de beurt! Het woord begint met: {beginletter}")

def foutieve_lengte():
    print("Fout: Het woord moet dezelfde lengte hebben!")

def gefeliciteerd(team):
    print(f"Gefeliciteerd {team}, het woord was correct!")

def helaas(team, te_raden_woord):
    print(f"Helaas {team}, het woord was: {te_raden_woord}")

def groene_bal_getrokken(team):
    print(f"{team} heeft een groene bal getrokken!")

def rode_bal_getrokken(team):
    print(f"{team} heeft een rode bal getrokken!")

def nummer_getrokken(team, nummer):
    print(f"{team} heeft balnummer {nummer} getrokken!")

def toon_bingokaart(team, kaart):
    print(f"Bingo-kaart van {team}:")
    for rij in kaart:
        print(" ".join(str(getal) if getal != 0 else "_" for getal in rij))

def einde_spel(team):
    print(f"Einde spel! {team} wint!")

def opnieuw_spelen_prompt():
    return input("Wil je opnieuw spelen? (ja/nee): ").strip().lower()

def raad_woord_prompt(geraden_letters):
    print("Raad het woord: ", " ".join(geraden_letters))
    return input("Jouw gok: ").lower()