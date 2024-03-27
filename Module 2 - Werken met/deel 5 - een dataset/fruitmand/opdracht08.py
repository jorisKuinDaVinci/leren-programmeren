import fruitmand
#Print alleen het gewicht van de volledige fruitmand.
for fruit in fruitmand.fruitmand:
    print(fruit['weight'])
#Voeg daarna (met code) een watermeloen toe aan de fruitmand en print daarna alleen het gewicht van de volledige fruitmand.
fruitmand.fruitmand.append({'name': 'watermeloen', 'weight': 5, 'round': True})
for fruit in fruitmand.fruitmand:
    print(fruit['weight'])