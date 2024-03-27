import fruitmand
#vraag om een aantal
aantal = input("Hoeveel fruit wil je zien? ")
#Print het opgegeven aantal keer een random fruitnaam uit de fruitmand. (dus bijv. niet 10 x appel)
for i in range(int(aantal)):
    print(fruitmand.fruitmand[i]['name'])