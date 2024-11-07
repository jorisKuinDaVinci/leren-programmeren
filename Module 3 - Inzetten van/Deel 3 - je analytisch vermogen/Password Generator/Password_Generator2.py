import string
import random

opnieuw = True
kleine_letters = string.ascii_lowercase
hoofdletters = string.ascii_uppercase
speciale_tekens = '@#$%&_?'
cijfers = '0123456789'

while opnieuw == True:
    randomhoofdletters = random.randint(2,6)
    randomgetallen = random.randint(4,7)
    randomletters = random.randint(8,10)
    wachtwoord = ''
    
    for x in range(8):
        wachtwoord += random.choice(kleine_letters)

    for x in range(randomhoofdletters):
        wachtwoord += random.choice(hoofdletters)

    for x in range(3):
        wachtwoord += random.choice(speciale_tekens)

    for x in range(randomgetallen):
        wachtwoord += random.choice(cijfers)

    wachtwoord = ''.join(random.sample(wachtwoord, len(wachtwoord)))
    
    if len(wachtwoord) == 24:
        if wachtwoord[11] and wachtwoord[12] not in hoofdletters:
            if wachtwoord[23] not in kleine_letters:
                if wachtwoord[0] and wachtwoord[23] not in speciale_tekens:
                    if wachtwoord[0] and wachtwoord[1] and wachtwoord[2] not in cijfers:
                        opnieuw = False
                        print(wachtwoord)
    else:
        ()