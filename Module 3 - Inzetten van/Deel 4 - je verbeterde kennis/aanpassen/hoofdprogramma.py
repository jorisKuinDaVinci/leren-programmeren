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
    # Keuze 1: splitsing
    keuze_1 = vraag_invoer("Je staat voor een splitsing, welke kant kies je? (links of rechts): ", ["links", "rechts"])
    if not controleer_antwoord(keuze_1, "1"):
        print("Je kiest links en een beer eet je op.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je loopt verder en komt aan bij een huis.")

    # Keuze 2: aanbellen of weglopen
    keuze_2 = vraag_invoer("Wat doe je? (aanbellen of weglopen): ", ["aanbellen", "weglopen"])
    if keuze_2 == "aanbellen":
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

    # Keuze 3: zwemmen of brug
    keuze_3 = vraag_invoer("Wat doe je? (zwemmen of brug): ", ["zwemmen", "brug"])
    if not controleer_antwoord(keuze_3, "5"):
        print("De brug stort in. Je valt in het water en verdrinkt.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je zwemt naar de overkant en loopt verder.")

    # Keuze 4: oversteken of bos
    keuze_4 = vraag_invoer("Wat doe je? (oversteken of bos): ", ["oversteken", "bos"])
    if not controleer_antwoord(keuze_4, "6"):
        print("Je kiest oversteken en wordt aangereden door een auto.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je loopt verder door het bos en komt bij een zebrapad.")

    # Keuze 5: oversteken of wachten
    keuze_5 = vraag_invoer("Wat doe je? (oversteken of wachten): ", ["oversteken", "wachten"])
    if not controleer_antwoord(keuze_5, "7"):
        print("Je kiest wachten en wordt neergeschoten door een jager.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je steekt over en komt aan bij een huis met een bordje 'te koop'.")

    # Keuze 6: huis kopen of verder lopen
    keuze_6 = vraag_invoer("Wat doe je? (huis of verder): ", ["huis", "verder"])
    if not controleer_antwoord(keuze_6, "8"):
        print("Je koopt het huis en sterft later aan een ziekte.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je loopt verder en komt bij een kruispunt.")

    # Keuze 7: links of rechts
    keuze_7 = vraag_invoer("Welke kant kies je? (links of rechts): ", ["links", "rechts"])
    if not controleer_antwoord(keuze_7, "9"):
        print("Je kiest links en loopt in een berenval.")
        antwoorden_correct = False
        print_game_over()
        return

    print("Je kiest rechts en vindt het einde van het bos.")

    # Controleer of alle antwoorden correct zijn
    if antwoorden_correct:
        print(TEKSTEN["gewonnen"])

# Start het avontuur
if __name__ == "__main__":
    avontuur()