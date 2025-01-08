from functions_Papi_Gelato import (
    vraag_klant_type_via_invoer,
    zakelijke_klant_workflow,
    particulier_workflow
)

def main():
    """Hoofdprogramma van de applicatie."""
    while True:
        # Vraag het klanttype
        klant_type = vraag_klant_type_via_invoer()

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

        if klant_type == "zakelijk":
            bestellingen = {
                "liters": 0,
                "smaken": {"Aardbei": 0, "Chocolade": 0, "Vanille": 0},
            }
            zakelijke_klant_workflow(bestellingen)
            break


if __name__ == "__main__":
    main()