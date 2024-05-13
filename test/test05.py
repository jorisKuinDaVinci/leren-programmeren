x = 3 # variable/ value of waarde

kleuren = ('paars', 'geel', 'rood', 'geel')

# kleuren onder elkaar
for kleur in kleuren:
    print(kleur)  

# hoeveel gele mn`s

aantal_geel = 0
for kleur in kleuren:
    if kleur == 'geel':
        aantal_geel += 1

print(aantal_geel)

print(kleuren.count('geel'))

# voor elke kleur hoeveel keer komt het voor
kleuren_teller = {}
for kleur in kleuren:
    if kleur in kleuren_teller:
        kleuren_teller[kleur] += 1
    else:
        kleuren_teller[kleur] = 1

print(kleuren_teller)