import fruitmand

#Print (met code) de namen en het gewicht in kilogram van het fruit op volgorde van gewicht (zwaarste bovenaan).
sorted_fruitmand = sorted(fruitmand.fruitmand, key=lambda x: x['weight'], reverse=True)


for fruit in sorted_fruitmand:
    print(fruit['name'], fruit['weight'] / 1000)