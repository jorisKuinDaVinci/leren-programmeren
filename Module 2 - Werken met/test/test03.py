lijst = [5, 5, 3, 2, 15]
tuple = (5, 3, 2, 15)
mijn_set = set(lijst) # unieke items en zonder gegarandeerde volgorde
getal = int('5')
mijn_dict = {'naam': 'Lithe', 
        'leeftijd': 21,
        'kleur_ogen': 'bruin'} # om iets te omschrijven of bijv. iets te tellen!

print(lijst)
print(mijn_set)
print(mijn_dict['naam'])

# print de complete persoon bijv:
# naam: Lithe
# leeftijd: 21
# kleur_ogen: bruin

for sleutel, waarde in mijn_dict.items():
    print(f'{sleutel}: {waarde}')

for sleutel in mijn_dict.keys():
    print(sleutel)

for sleutel in mijn_dict.values():
    print(sleutel)    

# controleer of een bepaalde sleutel in een dict zit!
mijn_kleuren = {'rood': 2, 'groen': 3, 'blauw': 0}
# zit er blauw in?
if 'blauw' in mijn_kleuren:
    print('er zit blauw in!')

# hoe voeg ik een item toe aan een dict?
mijn_kleuren.update({'paars': 0})
print(mijn_kleuren)