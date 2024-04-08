import fruitmand
#Print vanuit de fruitmand alleen het gewicht van de appel, gebruik maximaal 4 regels code (minus lege regels en de import).
# zorg er voor dat het ook werkt als het op een andere regel staat.
fruitmand = fruitmand.fruitmand
for fruit in fruitmand:
    if fruit["naam"] == "appel":
        print(fruit["gewicht"])