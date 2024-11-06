import random
import string

def genereer_wachtwoord():
    # Defineer de karakter sets
    hoofdletters = string.ascii_uppercase
    kleine_letters = string.ascii_lowercase
    speciale_tekens = "@#$%&_?"
    cijfers = string.digits

    # Random aantal hoofdletters (tussen 2 en 6)
    aantal_hoofdletters = random.randint(2, 6)
    gekozen_hoofdletters = random.sample(hoofdletters, aantal_hoofdletters)

    # Zorg ervoor dat hoofdletters niet op de middelste posities (11 en 12 in een 24-karakter wachtwoord) staan
    posities_hoofdletters = []
    while len(posities_hoofdletters) < aantal_hoofdletters:
        positie = random.randint(0, 23)
        if positie not in [11, 12] and positie not in posities_hoofdletters:
            posities_hoofdletters.append(positie)

    # Minimaal 8 kleine letters
    aantal_kleine_letters = 24 - aantal_hoofdletters - 3 - 4  # Zorgt dat er genoeg ruimte is voor cijfers en speciale tekens
    gekozen_kleine_letters = random.sample(kleine_letters, max(8, aantal_kleine_letters))

    # Zorg ervoor dat het wachtwoord niet eindigt met een kleine letter
    laatste_positie = random.choice([False, True])
    if laatste_positie:
        gekozen_kleine_letters[-1], gekozen_hoofdletters[0] = gekozen_hoofdletters[0], gekozen_kleine_letters[-1]

    # 3 speciale tekens, niet op de eerste of laatste positie
    gekozen_speciale_tekens = random.sample(speciale_tekens, 3)
    posities_speciale_tekens = []
    while len(posities_speciale_tekens) < 3:
        positie = random.randint(1, 22)  # Niet op de eerste (0) of laatste (23) positie
        if positie not in posities_speciale_tekens and positie not in posities_hoofdletters:
            posities_speciale_tekens.append(positie)

    # Random aantal cijfers tussen 4 en 7, niet op de eerste 3 posities
    aantal_cijfers = random.randint(4, 7)
    gekozen_cijfers = random.sample(cijfers, aantal_cijfers)
    posities_cijfers = []
    while len(posities_cijfers) < aantal_cijfers:
        positie = random.randint(3, 23)  # Geen cijfers op de eerste drie posities
        if positie not in posities_cijfers and positie not in posities_speciale_tekens and positie not in posities_hoofdletters:
            posities_cijfers.append(positie)

    # Plaats alle karakters op hun toegewezen posities in een lijst van 24 elementen
    wachtwoord_lijst = [""] * 24
    for i, letter in zip(posities_hoofdletters, gekozen_hoofdletters):
        wachtwoord_lijst[i] = letter
    for i, letter in zip(posities_speciale_tekens, gekozen_speciale_tekens):
        wachtwoord_lijst[i] = letter
    for i, cijfer in zip(posities_cijfers, gekozen_cijfers):
        wachtwoord_lijst[i] = cijfer

    # Vul de overige lege posities met kleine letters
    kleine_letter_posities = [i for i in range(24) if wachtwoord_lijst[i] == ""]
    for i, letter in zip(kleine_letter_posities, gekozen_kleine_letters):
        wachtwoord_lijst[i] = letter

    # Zet de lijst om in een string
    wachtwoord = "".join(wachtwoord_lijst)
    return wachtwoord

# Genereer en toon een wachtwoord
print(genereer_wachtwoord())