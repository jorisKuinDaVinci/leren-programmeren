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
    gekozen_kleine_letters = random.sample(kleine_letters, aantal_kleine_letters)

    # Random speciale tekens
    gekozen_speciale_tekens = random.sample(speciale_tekens, 3)

    # Initialiseer het wachtwoord als een lijst van lege tekens
    wachtwoord_lijst = [""] * 24

    # Plaats hoofdletters, vermijd posities 11 en 12
    hoofdletter_posities = random.sample([i for i in range(24) if i not in [11, 12]], aantal_hoofdletters)
    for i in range(aantal_hoofdletters):
        wachtwoord_lijst[hoofdletter_posities[i]] = gekozen_hoofdletters[i]

    # Plaats speciale tekens, vermijd de eerste en laatste positie
    speciale_tekens_posities = random.sample([i for i in range(1, 23)], 3)
    for i in range(3):
        wachtwoord_lijst[speciale_tekens_posities[i]] = gekozen_speciale_tekens[i]

    # Plaats cijfers, vermijd de eerste drie posities
    cijfers_posities = random.sample([i for i in range(3, 24)], aantal_cijfers)
    for i in range(aantal_cijfers):
        wachtwoord_lijst[cijfers_posities[i]] = gekozen_cijfers[i]

    # Vul de overige posities met kleine letters
    lege_posities = [i for i in range(24) if wachtwoord_lijst[i] == ""]
    for i in range(len(lege_posities)):
        wachtwoord_lijst[lege_posities[i]] = gekozen_kleine_letters[i]

    # Zorg ervoor dat de laatste positie geen kleine letter is
    if wachtwoord_lijst[-1] in kleine_letters:
        wachtwoord_lijst[-1] = random.choice(hoofdletters + cijfers + speciale_tekens)

    # Zet de lijst om in een string
    wachtwoord = "".join(wachtwoord_lijst)
    return wachtwoord

# Genereer en toon een wachtwoord
print(genereer_wachtwoord())