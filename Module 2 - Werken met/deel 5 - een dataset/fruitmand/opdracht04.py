import fruitmand
from random import choice
fruitmand_opdracht = fruitmand.fruitmand
#vraag om een aantal
try:
    aantal = int(input("Hoeveel fruit wil je zien? "))
except ValueError:
    print("Dat is geen geldige invoer")
    exit()
#Print het opgegeven aantal keer een random fruitnaam uit de fruitmand. (dus bijv. niet 10 x appel) echt random!
for i in range(aantal):
    fruit = choice(fruitmand_opdracht)
    print(fruit['name'])
#for i in range(int(aantal)):
    #print(fruitmand.fruitmand[i]['name'])