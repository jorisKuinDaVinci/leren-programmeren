# een functie die twee getallen binnenkrijgt en vervolgens de kleinste van de 2 teruggeeft
# BIF = Build In Function
def get_smallest(getal1: int, getal2: int) -> str: # een functie kun je 1 of meer parameters meegeven!
    #pass
    kleinste = 0
    if getal1 < getal2:
        kleinste = getal1
        #print("het kleinste getal is: " + str(kleinste))
    else:
        kleinste = getal2
        #print("het kleinste getal is: " + str(kleinste))

    #return kleinste
    return f"het kleinste getal is: {kleinste}" # geeft terug: het kleinste getal is: x

# enentuele variabelen/ constantes

# programma code
print(get_smallest(2, 4))  # argumenten  
print(get_smallest(6, 5))  # argumenten  
print(get_smallest(15, 15))  # argumenten 

# deze code werkt