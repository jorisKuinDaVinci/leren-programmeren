try: klein = int(input("hoeveel klein?"))
except: print("error")
try: medium = int(input("hoeveel medium?"))
except: print("error")
try: groot = int(input("hoeveel groot?"))
except: print("error")
try: PIZZA_PRIJZEN = {
    "klein": 5.00,
    "medium": 7.00,
    "groot": 10.00
}
except: print("error")
try: print(type(PIZZA_PRIJZEN))
except: print("error")

try: kosten_klein = klein * PIZZA_PRIJZEN["klein"]
except: print("error")
try: kosten_medium = medium * PIZZA_PRIJZEN["medium"]
except: print("error")
try: kosten_groot = groot * PIZZA_PRIJZEN["groot"]
except: print("error")

try: totaal = kosten_klein + kosten_medium + kosten_groot
except: print("error")
#print(f"De kosten zijn {totaal:.2f} euro voor {klein} kleine pizza's, {medium} medium pizza's en {groot} grote pizza's")
print("----------------------------------------------------")
try: print("|  Klein     : " + str(klein))
except: print("error")
try: print("|  kosten klein  : " + str(kosten_klein))
except: print("error")
try: print("|  medium  : " + str(medium))
except: print("error")
try: print("|  kosten medium: " + str(kosten_medium))
except: print("error")
try: print("|  Groot  : " + str(groot))
except: print("error")
try: print("|  kosten groot: " + str(kosten_groot))
except: print("error")
print("----------------------------------------------------")
try: print("|  Totaal: " + str(totaal))
except: print("error")