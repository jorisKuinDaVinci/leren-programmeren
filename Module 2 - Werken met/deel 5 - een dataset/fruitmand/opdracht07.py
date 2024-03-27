import fruitmand
#Print alleen de namen van het fruit in de fruitmand die rond zijn, gebruik maximaal 4 regels code (minus lege regels en de import).
for fruit in fruitmand.fruitmand:
    if fruit['round'] == True:
        print(fruit['name'])