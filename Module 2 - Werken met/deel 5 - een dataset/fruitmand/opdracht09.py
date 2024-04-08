from fruitmand import fruitmand

#Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, in maximaal 8 regels code (minus lege regels en de import).
# zorg er voor dat het ook werkt als het op een andere regel staat.
fruitmand_opdracht = fruitmand
print(fruitmand_opdracht)
# zoek plaats van de druif.
for i in range(len(fruitmand_opdracht)):
    if fruitmand_opdracht[i]['name'] == 'druif':
        # verwijder de druif uit de fruitmand
        fruitmand_opdracht.pop(i)
        break
print(fruitmand_opdracht)
#print alle verschillende kleuren in de fruitmand
kleuren = set()
for fruit in fruitmand_opdracht:
    kleuren.add(fruit['color'])
for color in kleuren:
    print(color)
print(fruitmand_opdracht)
