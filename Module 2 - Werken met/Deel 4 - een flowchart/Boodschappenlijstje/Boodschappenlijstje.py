Boodschappenlijstje = {}
welk_artikel = input("Welk artikel wil je toevoegen?")
hoeveelheid = input("Hoeveel wil je toevoegen?")
def check_item(welk_artikel):
    if welk_artikel in Boodschappenlijstje:
        Boodschappenlijstje[welk_artikel] += int(hoeveelheid)
        return True
    else:
        Boodschappenlijstje[welk_artikel] = int(hoeveelheid)
        return False
check_item(welk_artikel)
nog_meer_toevoegen = input("Wil je nog meer toevoegen? (ja/nee)")
while nog_meer_toevoegen == "ja":
    welk_artikel = input("Welk artikel wil je toevoegen?")
    hoeveelheid = input("Hoeveel wil je toevoegen?")
    check_item(welk_artikel)
    nog_meer_toevoegen = input("Wil je nog meer toevoegen? (ja/nee)")
if nog_meer_toevoegen == "nee":
    print("------------------boodschappenlijstje-------------------------------")
    for value, key in Boodschappenlijstje.items():
        print(value, key)  
    print("-------------------------------------------------------------------")
