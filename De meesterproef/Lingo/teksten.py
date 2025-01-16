def print_introductie():
    """Print de introductietekst voor het spel."""
    print("Welkom bij Lingo! Het doel is om het juiste woord te raden.")


def print_beurt_start(team, beginletter):
    """Print welke team aan de beurt is en de beginletter van het woord."""
    print(f"\n{team} is aan de beurt! Het woord begint met: {beginletter}")


def print_fout_woord_lengte():
    """Print een foutmelding als het ingevoerde woord niet de juiste lengte heeft."""
    print("Fout: Het woord moet dezelfde lengte hebben als het te raden woord!")


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