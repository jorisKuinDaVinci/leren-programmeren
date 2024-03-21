Boodschappenlijstje = {}
welk_artikel = input("Welk artikel wil je toevoegen?")
hoeveelheid_toevoegen = input("Hoeveel wil je toevoegen?")
def check_item(welk_artikel):
    if welk_artikel.lower() in Boodschappenlijstje:
        Boodschappenlijstje[welk_artikel] += int(hoeveelheid_toevoegen)
        return True
    if welk_artikel.upper() in Boodschappenlijstje:
        Boodschappenlijstje[welk_artikel] += int(hoeveelheid_toevoegen)
        return True
    if welk_artikel.capitalize() in Boodschappenlijstje:
        Boodschappenlijstje[welk_artikel] += int(hoeveelheid_toevoegen)
        return True
    if welk_artikel in Boodschappenlijstje:
        Boodschappenlijstje[welk_artikel] += int(hoeveelheid_toevoegen)
        return True
    else:
        Boodschappenlijstje[welk_artikel] = int(hoeveelheid_toevoegen)
        return False
check_item(welk_artikel)
nog_meer_toevoegen = input("Wil je nog meer toevoegen? (ja/nee)")
while nog_meer_toevoegen == "ja":
    welk_artikel = input("Welk artikel wil je toevoegen?")
    hoeveelheid_toevoegen = input("Hoeveel wil je toevoegen?")
    check_item(welk_artikel)
    nog_meer_toevoegen = input("Wil je nog meer toevoegen? (ja/nee)")
if nog_meer_toevoegen == "nee":
    print("------------------boodschappenlijstje-------------------------------")
    for artikel, hoeveel in Boodschappenlijstje.items():
        print(artikel, "x", hoeveel)  
    print("-------------------------------------------------------------------")
