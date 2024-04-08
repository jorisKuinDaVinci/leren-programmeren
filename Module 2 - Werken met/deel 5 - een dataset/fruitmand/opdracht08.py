from fruitmand import fruitmand
#Print alleen het totale gewicht van de volledige fruitmand.

totale_gewicht = sum(fruit['weight'] for fruit in fruitmand)
print(totale_gewicht)
#Voeg daarna (met code) een watermeloen toe aan de fruitmand en print daarna alleen het gewicht van de volledige fruitmand.
fruitmand.append({'name': 'watermeloen', 'weight': 2500, 'round': True})
totale_gewicht = sum(fruit['weight'] for fruit in fruitmand)
print(totale_gewicht)