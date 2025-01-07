from functions_Papi_Gelato import (
    vraag_invoer,
    #vraag_aantal_bolletjes,
    #controleer_aantal_bolletjes,
    #vraag_smaak,
    #controleer_smaak,
    #vraag_hoorntje_of_bakje,
    #controleer_keuze,
    #vraag_topping,
    #controleer_topping,
    #bereken_topping_prijs,
    #bevestiging_bestelling,
    #print_bon,
    #vraag_klant_type,
    controleer_klant_type,
    zakelijke_klant_workflow,
    particulier_workflow
)

from data_Papi_Gelato import TEKSTEN


# Functie om bestellingen te resetten
def reset_bestellingen():
    return {
        "bolletjes": 0,
        "hoorntjes": 0,
        "bakjes": 0,
        "smaken": {
            "Aardbei": 0,
            "Chocolade": 0,
            "Munt": 0,
            "Vanille": 0,
        },
        "topping_prijs": 0.0
    }


def main():
    print(TEKSTEN["welkom_tekst"])

    # Vraag naar klanttype
    klant_type = vraag_invoer(TEKSTEN["vraag_klant_type"], [controleer_klant_type])

    bestellingen = reset_bestellingen()

    # Afhankelijk van klanttype: zakelijke of particuliere workflow
    if klant_type == "zakelijk":
        zakelijke_klant_workflow(bestellingen)
    elif klant_type == "particulier":
        particulier_workflow(bestellingen)

    # Vraag om meer te bestellen
    while True:
        print(TEKSTEN["vraag_nog_meer"])
        antwoord = input("> ")
        if antwoord.lower() == "ja":
            bestellingen = reset_bestellingen()
            if klant_type == "zakelijk":
                zakelijke_klant_workflow(bestellingen)
            else:
                particulier_workflow(bestellingen)
        else:
            print(TEKSTEN["afsluit_tekst"])
            break


if __name__ == "__main__":
    main()