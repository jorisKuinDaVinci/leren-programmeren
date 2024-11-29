# hoofdprogramma.py

from functions import vraag_invoer, controleer_antwoord, print_game_over, print_introductie
from juiste_antwoorden import JUISTE_ANTWOORDEN, SPECIALE_SPELER, SPECIALE_ANTWOORDEN
from data import TEKSTEN

def avontuur():
    #De hoofdlogica van het avontuur.
    naam = input("Wat is je naam? ").strip()
    
    if naam.lower() == SPECIALE_SPELER.lower():
        print(f"Hallo {naam}, dit zijn de juiste antwoorden: {SPECIALE_ANTWOORDEN}")
    print_introductie(naam)
    print(TEKSTEN["start_tekst"])

    antwoorden_correct = True

    # Scenario 1: splitsing
    keuze = vraag_invoer("Je staat voor een splitsing, welke kant kies je? (links of rechts): ", ["links", "rechts"])
    if not controleer_antwoord(keuze, "1"):
        print("Je kiest links en een beer eet je op.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je loopt verder en komt aan bij een huis.")

    # Scenario 2: aanbellen of weglopen
    keuze = vraag_invoer("Wat doe je? (aanbellen of weglopen): ", ["aanbellen", "weglopen"])
    if keuze == "aanbellen":
        print("Er doet niemand open. Je probeert een code in te voeren.")
        code = input("Voer de code in: ").strip()
        if code != "104":
            print("Foutieve code. Het apparaat ontploft en je sterft.")
            antwoorden_correct = False
            print_game_over()
            return
        print("De deur gaat open. Je wordt uitgenodigd door een oude vrouw.")
    else:
        print("Je loopt weg en komt bij een rivier.")

    # Scenario 3: zwemmen of brug
    keuze = vraag_invoer("Wat doe je? (zwemmen of brug): ", ["zwemmen", "brug"])
    if not controleer_antwoord(keuze, "5"):
        print("De brug stort in. Je valt in het water en verdrinkt.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je zwemt naar de overkant en loopt verder.")
    # Scenario gaat verder zoals in de originele logica...

    # Winnaar bepalen
    if antwoorden_correct:
        print(TEKSTEN["gewonnen"])

# Start het avontuur
if __name__ == "__main__":
    avontuur()