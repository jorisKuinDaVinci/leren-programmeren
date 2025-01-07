from functions_Papi_Gelato import (
    vraag_klant_type,
    controleer_klant_type,
    zakelijke_klant_workflow,
    particulier_workflow
)


def main():
    # Start van de applicatie
    while True:
        print(vraag_klant_type())
        klant_type_keuze = input("> ").strip()
        klant_type = controleer_klant_type(klant_type_keuze)
        
        if klant_type == "particulier":
            bestellingen = {
                "bolletjes": 0,
                "hoorntjes": 0,
                "bakjes": 0,
                "smaken": {"Aardbei": 0, "Chocolade": 0, "Munt": 0, "Vanille": 0},
                "topping_prijs": 0.0
            }
            particulier_workflow(bestellingen)
            break
        elif klant_type == "zakelijk":
            bestellingen = {
                "liters": 0,
                "smaken": {"Aardbei": 0, "Chocolade": 0, "Munt": 0, "Vanille": 0},
            }
            zakelijke_klant_workflow(bestellingen)
            break
        else:
            print("Sorry dat snap ik niet...")

if __name__ == "__main__":
    main()