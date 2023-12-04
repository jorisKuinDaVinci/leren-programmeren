
klas = []
for _ in range(2):
    persoon = {}
    persoon['naam'] = input('wat is uw voornaam?')
    persoon['Tussenvoegsel'] = input('wat is uw tussenvoegsel?')
    persoon['achternaam'] = input('wat is uw achternaam?')
    persoon['leeftijd'] = int(input('wat is uw leeftijd?'))
    klas.append(persoon)


print(klas)
print(klas[1]['leeftijd'])