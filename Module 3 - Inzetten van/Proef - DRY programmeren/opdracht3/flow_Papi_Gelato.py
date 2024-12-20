from functions_Papi_Gelato import vraag_aantal_bolletjes, controleer_aantal_bolletjes, vraag_smaak, controleer_smaak, vraag_hoorntje_of_bakje, controleer_keuze, bevestiging_bestelling, vraag_nog_meer, controleer_meer_bestellen, print_bon
from data_Papi_Gelato import TEKSTEN

print(TEKSTEN["welkom_tekst"])

# Bestellingen bijhouden
bestellingen = {
    "bolletjes": 0,
    "hoorntjes": 0,
    "bakjes": 0,
    "smaken": {
        "Aardbei": 0,
        "Chocolade": 0,
        "Munt": 0,
        "Vanille": 0,
    },
}

while True:
    print(vraag_aantal_bolletjes())
    aantal_input = input("> ")
    status, aantal = controleer_aantal_bolletjes(aantal_input)

    if status == "stap2":
        #smaken = []
        for i in range(1, aantal + 1):
            while True:
                print(vraag_smaak(i))
                smaak = input("> ")
                gekozen_smaak = controleer_smaak(smaak)
                if gekozen_smaak:
                    #smaken.append(gekozen_smaak)
                    bestellingen["smaken"][gekozen_smaak] += 1
                    break
                else:
                    print("Sorry dat snap ik niet...")

        while True:
            print(vraag_hoorntje_of_bakje(aantal))
            keuze = input("> ")
            keuze = controleer_keuze(keuze)
            if keuze:
                print(bevestiging_bestelling(keuze, aantal))
                bestellingen["bolletjes"] += aantal
                if keuze == "hoorntje":
                    bestellingen["hoorntjes"] += 1
                elif keuze == "bakje":
                    bestellingen["bakjes"] += 1
                break
            else:
                print("Sorry, dat snap ik niet...")
    elif status == "bakje":
        #smaken = []
        for i in range(1, aantal + 1):
            while True:
                print(vraag_smaak(i))
                smaak = input("> ")
                gekozen_smaak = controleer_smaak(smaak)
                if gekozen_smaak:
                    #smaken.append(gekozen_smaak)
                    bestellingen["smaken"][gekozen_smaak] += 1
                    break
                else:
                    print("Sorry dat snap ik niet...")
        print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes.")
        bestellingen["bolletjes"] += aantal
        bestellingen["bakjes"] += 1
    elif status == "teveel":
        print("Sorry, zulke grote bakken hebben we niet.")
        continue
    elif status == "ongeldig":
        print("Sorry, dat snap ik niet...")
        continue

    while True:
        print(vraag_nog_meer())
        meer_input = input("> ")
        meer = controleer_meer_bestellen(meer_input)
        if meer is True:
            break
        elif meer is False:
            print_bon(bestellingen)
            exit()
        else:
            print("Sorry, dat snap ik niet...")