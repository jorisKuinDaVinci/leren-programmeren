lijst = ["persoon2", "persoon1", "joris"]
# lijst aan de functie geven
# een hele lang zin. keer onder elkaar tot alle namen er staan.
# begin met leert programeren
def functie(lijst):
    zin = ""
    for naam in lijst:
        zin += naam + " leert programeren\n"
    return zin
print(functie(lijst))