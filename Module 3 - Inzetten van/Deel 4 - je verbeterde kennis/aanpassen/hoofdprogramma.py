from functions import vraag_invoer, controleer_antwoord, print_game_over, print_introductie
from juiste_antwoorden import JUISTE_ANTWOORDEN, SPECIALE_SPELER, SPECIALE_ANTWOORDEN, JUISTE_CODE
from data import TEKSTEN

#De hoofdlogica van het avontuur.
naam = input("Wat is je naam? ").strip()
    
if naam.lower() == SPECIALE_SPELER.lower():
    print(f"Hallo {naam}, dit zijn de juiste antwoorden: {SPECIALE_ANTWOORDEN}")
print_introductie(naam)
print(TEKSTEN["start_tekst"])

# Keuze 1: splitsing
def keuze_1():
    keuze = vraag_invoer("Je staat voor een splitsing, welke kant kies je? (links of rechts): ", ["links", "rechts"])
    if not controleer_antwoord(keuze, "1"):
        print("Je kiest links en een beer eet je op.")
        print_game_over()
        return
    print("Je loopt verder en komt aan bij een huis.")

# start keuze 1
keuze_1()

# Keuze 2: aanbellen of weglopen
def keuze_2():
    keuze = vraag_invoer("Wat doe je? (aanbellen of weglopen): ", ["aanbellen", "weglopen"])
    if keuze == "aanbellen":
        print("Er doet niemand open. Je probeert een code in te voeren.")
        if naam.lower() == SPECIALE_SPELER.lower():
            print(f"Hallo {naam}, dit is de juiste code: {JUISTE_CODE}")
        code = input("Voer de code in: ").strip()
        if code != "104":
            print("Foutieve code. Het apparaat ontploft.")
            print("Je loopt weg en komt bij een rivier.")
        if code == "104":
            print("De deur gaat open. Je wordt uitgenodigd door een oude vrouw.")
            print("Ze geeft je een kaart met de route naar huis.")
            print(TEKSTEN["gewonnen"])
            return
    else:
        print("Je loopt weg en komt bij een rivier.")

# start keuze 2
keuze_2()

# Keuze 3: zwemmen of brug
def keuze_3():
    keuze = vraag_invoer("Wat doe je? zwemmen (zwemmen) of over de brug lopen (brug).: ", ["zwemmen", "brug"])
    if not controleer_antwoord(keuze, "5"):
        print("De brug stort in. Je valt in het water.")
        print_game_over()
        return
    print("Je zwemt naar de overkant en loopt verder.")
    
# start keuze 3
keuze_3()

# Keuze 4: oversteken of door het bos lopen
def keuze_4():
    keuze = vraag_invoer("Wat doe je? oversteken (oversteken) of door het bos lopen (bos).: ", ["oversteken", "bos"])
    if not controleer_antwoord(keuze, "6"):
        print("Je kiest oversteken en raakt verdwaald.")
        print_game_over()
        return
    print("Je loopt verder door het bos en komt bij een zebrapad.")

# start keuze 4
keuze_4()

# Keuze 5: oversteken of wachten
def keuze_5():
    keuze = vraag_invoer("Wat doe je? (oversteken of wachten): ", ["oversteken", "wachten"])
    if not controleer_antwoord(keuze, "7"):
        print("Je kiest wachten en een beer eet je op.")
        print_game_over()
        return
    print("Je steekt over en komt aan bij een huis met een bordje 'te koop'.")
    
# start keuze 5
keuze_5()

# Keuze 6: huis kopen of verder lopen
def keuze_6():
    keuze = vraag_invoer("Wat doe je? huis kopen (huis) of verder lopen (verder).: ", ["huis", "verder"])
    if not controleer_antwoord(keuze, "8"):
        print("Je koopt het huis en vindt nooit je weg terug.")
        print_game_over()
        return
    print("Je loopt verder en komt bij een kruispunt.")
    
# start keuze 6
keuze_6()

# Keuze 7: links of rechts
def keuze_7():
    keuze = vraag_invoer("Welke kant kies je? (links of rechts): ", ["links", "rechts"])
    if not controleer_antwoord(keuze, "9"):
        print("Je kiest links en loopt in een berenval.")
        print_game_over()
        return
    print("Je kiest rechts en vindt het einde van het bos.")
    
# start keuze 7
keuze_7()

# Controleer of alle antwoorden correct zijn
print(TEKSTEN["gewonnen"])