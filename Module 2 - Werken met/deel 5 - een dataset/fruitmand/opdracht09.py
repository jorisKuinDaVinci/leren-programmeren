import fruitmand
#Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, in maximaal 8 regels code (minus lege regels en de import).
fruitmand.fruitmand.pop(4)
colors = []
for fruit in fruitmand.fruitmand:
    if fruit['color'] not in colors:
        colors.append(fruit['color'])
        print(fruit['color'])