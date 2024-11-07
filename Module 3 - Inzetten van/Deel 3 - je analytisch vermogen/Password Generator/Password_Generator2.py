import random
import string

def genereer_wachtwoord():
    # Defineer de karaktersets
    hoofdletters = string.ascii_uppercase
    kleine_letters = string.ascii_lowercase
    speciale_tekens = "@#$%&_?"
    cijfers = string.digits

    # Random aantal hoofdletters (tussen 2 en 6)
    aantal_hoofdletters = random.randint(2, 6)
    gekozen_hoofdletters = random.sample(hoofdletters, aantal_hoofdletters)

    # Random aantal cijfers tussen 4 en 7
    aantal_cijfers = random.randint(4, 7)
    gekozen_cijfers = random.sample(cijfers, aantal_cijfers)

    # Bepaal het aantal kleine letters zodat er precies 3 speciale tekens zijn en de totale lengte 24 is
    aantal_kleine_letters = 24 - aantal_hoofdletters - aantal_cijfers - 3
    gekozen_kleine_letters = random.sample(kleine_letters, max(8, aantal_kleine_letters))

    # Random speciale tekens
    gekozen_speciale_tekens = random.sample(speciale_tekens, 3)

    # Plaatsing van karakters in het wachtwoord
    wachtwoord_lijst = [""] * 24

    # Plaats hoofdletters, vermijd posities 11 en 12
    vrije_posities = [i for i in range(24) if i not in [11, 12]]
    for letter in gekozen_hoofdletters:
        positie = random.choice(vrije_posities)
        wachtwoord_lijst[positie] = letter
        vrije_posities.remove(positie)

    # Plaats speciale tekens, vermijd eerste en laatste positie
    vrije_posities = [i for i in vrije_posities if i not in [0, 23]]
    for symbool in gekozen_speciale_tekens:
        positie = random.choice(vrije_posities)
        wachtwoord_lijst[positie] = symbool
        vrije_posities.remove(positie)

    # Plaats cijfers, vermijd de eerste drie posities
    vrije_posities = [i for i in vrije_posities if i >= 3]
    for cijfer in gekozen_cijfers:
        positie = random.choice(vrije_posities)
        wachtwoord_lijst[positie] = cijfer
        vrije_posities.remove(positie)

    # Vul de overige posities met kleine letters
    for letter in gekozen_kleine_letters:
        if vrije_posities:
            positie = vrije_posities.pop(0)
            wachtwoord_lijst[positie] = letter

    # Controleer of de laatste positie een kleine letter bevat en wissel deze indien nodig
    if wachtwoord_lijst[-1] in kleine_letters:
        # Wissel met een willekeurige hoofdletter of speciaal teken
        for i, char in enumerate(wachtwoord_lijst):
            if char in hoofdletters + speciale_tekens:
                wachtwoord_lijst[-1], wachtwoord_lijst[i] = wachtwoord_lijst[i], wachtwoord_lijst[-1]
                break

    # Zet de lijst om in een string
    wachtwoord = "".join(wachtwoord_lijst)
    return wachtwoord

# Genereer en toon een wachtwoord
print(genereer_wachtwoord())