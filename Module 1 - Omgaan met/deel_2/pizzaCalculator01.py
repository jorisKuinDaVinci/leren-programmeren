klein = int(input("hoeveel klein?"))
medium = int(input("hoeveel medium?"))
groot = int(input("hoeveel groot?"))
PIZZA_PRIJZEN = {
    "klein": 5.00,
    "medium": 7.00,
    "groot": 10.00
}

kosten_klein = klein * PIZZA_PRIJZEN["klein"]
kosten_medium = medium * PIZZA_PRIJZEN["medium"]
kosten_groot = groot * PIZZA_PRIJZEN["groot"]

totaal = kosten_klein + kosten_medium + kosten_groot
#print(f"De kosten zijn {totaal:.2f} euro voor {klein} kleine pizza's, {medium} medium pizza's en {groot} grote pizza's")
print("----------------------------------------------------")
print("|  Klein     : " + str(klein))
print("|  kosten klein  : " + str(kosten_klein))
print("|  medium  : " + str(medium))
print("|  kosten medium: " + str(kosten_medium))
print("|  Groot  : " + str(groot))
print("|  kosten groot: " + str(kosten_groot))
print("----------------------------------------------------")
print("|  Totaal: " + str(totaal))