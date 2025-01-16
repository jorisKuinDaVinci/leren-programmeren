def print_introductie():
    """Print de introductietekst."""
    print("Welkom bij het Lingo-spel! Twee teams gaan de strijd aan.")


def print_beurt_start(team, beginletter):
    """Print dat een team aan de beurt is met de beginletter van het woord."""
    print(f"\n{team} is aan de beurt! Het woord begint met: {beginletter}")


def print_fout_woord_lengte():
    """Print een foutmelding als het ingevoerde woord niet de juiste lengte heeft."""
    print("Fout: Het woord moet dezelfde lengte hebben als het te raden woord!")


def print_winnaar(team):
    """Print welke team het spel wint."""
    print(f"Einde spel! {team} wint!")


def print_afsluiting():
    """Print een afsluitende tekst."""
    print("Bedankt voor het spelen! Tot de volgende keer!")


def vraag_opnieuw_spelen():
    """Vraag de speler of ze opnieuw willen spelen."""
    antwoord = input("Wil je opnieuw spelen? (ja/nee): ").lower()
    return antwoord == "ja"