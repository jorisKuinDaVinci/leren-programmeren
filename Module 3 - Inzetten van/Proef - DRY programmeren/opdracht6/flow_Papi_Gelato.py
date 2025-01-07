from functions_Papi_Gelato import (
    vraag_invoer,
    controleer_klant_type,
    zakelijke_klant_workflow,
    particulier_workflow
)

from data_Papi_Gelato import TEKSTEN

def main():
    """Hoofdprogramma van de applicatie."""
    while True:
        klant_type = vraag_invoer(
            TEKSTEN["vraag_klant_type"],
            [controleer_klant_type]
        )

        if klant_type == "particulier":
            bestellingen = {
                "bolletjes": 0,
                "hoorntjes": 0,
                "bakjes": 0,
                "smaken": {"Aardbei": 0, "Chocolade": 0, "Vanille": 0},
                "topping_prijs": 0.0
            }
            particulier_workflow(bestellingen)
            break

        elif klant_type == "zakelijk":
            bestellingen = {
                "liters": 0,
                "smaken": {"Aardbei": 0, "Chocolade": 0, "Vanille": 0},
            }
            zakelijke_klant_workflow(bestellingen)
            break


if __name__ == "__main__":
    main()