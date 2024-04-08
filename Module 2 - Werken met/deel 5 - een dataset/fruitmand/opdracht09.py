import fruitmand
#Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, in maximaal 8 regels code (minus lege regels en de import).
# zorg er voor dat het ook werkt als het op een andere regel staat.
fruitmand = fruitmand.fruitmand
fruitmand.remove("druif")
kleuren = set()
for fruit in fruitmand:
    kleuren.add(fruit["kleur"])