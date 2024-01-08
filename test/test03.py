import string
import random
from random import randint, choice
# eisen password:
# lengte tussen 10 en 20
# start met een hoofdletter
# eindig met een kleine letter'
# vanaf karakter 3 komt er random 4 getallen met tussendoor random een hoofd of kleine letter

# ww 10: Aa1f3G4j7x
print(string.ascii_lowercase)
print(string.ascii_uppercase)

# random getal

password = ''

print(random.randint(0,9))
print(random.choice(string.ascii_uppercase))
print(random.choice(string.ascii_lowercase))

lengte = int(input('Geef de lengte van het wachtwoord(tussen 10 en 20): '))

while lengte < 10 or lengte > 20:
    lengte = int(input('Geef de lengte van het wachtwoord(tussen 10 en 20): '))

if lengte == 11:
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_lowercase)
    password += str(random.randint(0,9))
    password += random.choice(string.ascii_lowercase)
    password += str(random.randint(0,9))
    password += random.choice(string.ascii_uppercase)
    password += str(random.randint(0,9))
    password += random.choice(string.ascii_lowercase)
    password += str(random.randint(0,9))
    password += random.choice(string.ascii_lowercase)
elif lengte == 12:
    for x in range(12):
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_lowercase)
        password += str(random.randint(0,9))

print(f"Uw wachtwoord is: " + password)