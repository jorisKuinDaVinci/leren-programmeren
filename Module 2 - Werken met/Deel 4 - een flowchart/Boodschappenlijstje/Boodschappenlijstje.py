Boodschappenlijstje = {}
while True:
    welk_artikel = input("Welk artikel wil je toevoegen?").lower()
    hoeveelheid_toevoegen = input("Hoeveel wil je toevoegen?")
    if welk_artikel in Boodschappenlijstje:
        Boodschappenlijstje[welk_artikel] += int(hoeveelheid_toevoegen)
    else:
        Boodschappenlijstje[welk_artikel] = int(hoeveelheid_toevoegen)
    nog_meer_toevoegen = input("Wil je nog meer toevoegen? (ja/nee)")
    if nog_meer_toevoegen == "nee":
        break
print("------------------boodschappenlijstje-------------------------------")
for artikel, hoeveel in Boodschappenlijstje.items():
    print(artikel, "x", hoeveel)  
print("-------------------------------------------------------------------")