import fruitmand
from random import choice
fruitmand_kopie = fruitmand.fruitmand.copy()
#vraag om een aantal
aantal = int(input("Hoeveel fruit wil je zien? "))
#Print het opgegeven aantal keer een random fruitnaam uit de fruitmand. (dus bijv. niet 10 x appel) echt random!
for i in range(aantal):
    fruit = choice(fruitmand_kopie)
    print(fruit['name'])
#for i in range(int(aantal)):
    #print(fruitmand.fruitmand[i]['name'])