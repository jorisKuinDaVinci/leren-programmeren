from fruitmand import fruitmand
#Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, in maximaal 8 regels code (minus lege regels en de import).
# zorg er voor dat het ook werkt als het op een andere regel staat.
fruitmand_opdracht = fruitmand
# zoek plaats van de druif.
for i in range(len(fruitmand_opdracht)):
    if fruitmand_opdracht[i]['name'] == 'druif':
        # print de index van de druif
        print(i)
        # verwijder de druif uit de fruitmand
        fruitmand_opdracht.pop(i)
#print alle verschillende kleuren in de fruitmand
for fruit in fruitmand_opdracht:
    print(fruit['color'])