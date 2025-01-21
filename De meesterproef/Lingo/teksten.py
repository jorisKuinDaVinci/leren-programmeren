def print_introductie():
    """Print de introductietekst voor het spel."""
    print("Welkom bij Lingo! Het doel is om het juiste woord te raden.")


def print_beurt_start(team, beginletter):
    """Print welke team aan de beurt is en de beginletter van het woord."""
    print(f"\n{team} is aan de beurt! Het woord begint met: {beginletter}")


def print_winnaar(team):
    """Print een bericht wanneer een team wint."""
    print(f"Einde spel! {team} wint!")


def print_afsluiting():
    """Print een bericht bij het afsluiten van het spel."""
    print("Bedankt voor het spelen!")


def vraag_opnieuw_spelen():
    """Vraag of de spelers opnieuw willen spelen."""
    antwoord = input("Wil je opnieuw spelen? (ja/nee): ").lower()
    return antwoord == "ja"


def vraag_naam():
    """Vraag de naam van de speler."""
    return input("Wat is je naam? ").strip()


def print_geraden():
    """Bericht wanneer het woord correct is geraden."""
    print("Gefeliciteerd! Je hebt het woord geraden.")


def print_verkeerd_geraden():
    """Bericht wanneer het geraden woord incorrect is."""
    print("Niet correct, probeer het opnieuw.")


def print_helaas_geraden_woord(te_raden_woord):
    """Bericht wanneer het woord niet geraden is na 5 pogingen."""
    print(f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}")


def print_fout_woord_lengte(te_raden_woord):
    """Bericht wanneer de lengte van het geraden woord niet klopt."""
    print(f"Fout: het woord moet {len(te_raden_woord)} letters lang zijn.")

def toon_woord_geraden():
    print("Gefeliciteerd! Je hebt het woord geraden.")

def toon_woord_verkeerd():
    print("Niet correct, probeer het opnieuw.")

def toon_woord_fout(te_raden_woord):
    print(f"Helaas, je hebt het woord niet geraden. Het juiste woord was: {te_raden_woord}")

def toon_fout_woord_lengte(len_woord):
    print(f"Fout: het woord moet {len_woord} letters lang zijn.")   