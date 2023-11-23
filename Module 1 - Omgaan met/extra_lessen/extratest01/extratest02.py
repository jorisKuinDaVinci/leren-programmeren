#Schrijf een programma waarin je de gebruiker vraagt om namen in te voeren tot de gebruiker stop invoert. 
#Begin met een lege lijst. 
#Zit de naam nog niet in de lijst? -> toevoegen.
#Wel aanwezig? dan een melding zit er al in.
#Als de gebruiker stop invoert, dan print je alle namen uit de lijst.


namen = []
while True:
    naam = input("Voer een naam of stop in: ")
    if naam == "stop":
        for naam in namen:
            print(naam)    
        break
    else:
        if naam in namen:
            print("Zit er al in")
        else:
            namen.append(naam)
