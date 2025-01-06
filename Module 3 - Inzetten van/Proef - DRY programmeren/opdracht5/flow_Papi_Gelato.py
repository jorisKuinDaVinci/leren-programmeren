from functions_Papi_Gelato import (
    vraag_aantal_bolletjes,
    controleer_aantal_bolletjes,
    vraag_smaak,
    controleer_smaak,
    vraag_hoorntje_of_bakje,
    controleer_keuze,
    vraag_topping,
    controleer_topping,
    bereken_topping_prijs,
    bevestiging_bestelling,
    vraag_nog_meer,
    controleer_meer_bestellen,
    print_bon,
    vraag_klant_type,
    controleer_klant_type,
    zakelijke_klant_workflow,
    particulier_workflow,
)
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
    "topping_prijs": 0.0,
}

while True:
    # Vraag klanttype
    while True:
        print(vraag_klant_type())
        klant_type = input("> ")
        klant_type = controleer_klant_type(klant_type)
        if klant_type:
            break
        else:
            print("Sorry dat snap ik niet...")

    if klant_type == "zakelijk":
        zakelijke_klant_workflow(bestellingen)
    elif klant_type == "particulier":
        particulier_workflow(bestellingen)

    # Vraag of de klant nog meer wil bestellen
    while True:
        print(vraag_nog_meer())
        meer_input = input("> ")
        meer = controleer_meer_bestellen(meer_input)
        if meer is True:
            break  # Start een nieuwe bestelling
        elif meer is False:
            print_bon(bestellingen)  # Toon de bon en sluit af
            exit()
        else:
            print("Sorry, dat snap ik niet...")