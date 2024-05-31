lijst = ["vader", "moeder", "joris"]
# lijst aan de functie geven
# een hele lang zin. keer onder elkaar tot alle namen er staan.
# begin met leert programeren
def functie(lijst):
    zin = ""
    cijfer = 0
    for i in range(len(lijst)):
        zin += lijst[cijfer] + " leert programeren\n"
        cijfer += 1
    return zin
print(functie(lijst))