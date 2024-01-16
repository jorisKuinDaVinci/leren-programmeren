#schrijf de code om de volgende infomatie op te vragen en op te slaan in een dictionary:
# - automerk
# - model
# - prijs
# lijst met 5 auto`s

# print alleen 5 prijzen onder elkaar
automerkenextra = ["BMW", "Mercedes", "Audi", "Volkswagen", "Porsche", "Renault"]
autos = []
for _ in range(10):
    auto = {}
    auto['automerk'] = input('wat is het automerk?')
    auto['model'] = input('wat is het model?')
    auto['prijs'] = int(input('wat is de prijs?'))
    if auto['automerk'] in automerkenextra:
        autos.append(auto)
    else:
        print('automerk niet gevonden')
        break

for auto in autos:
    print(auto['automerk'])
    print(auto['model'])
    print(auto['prijs'])
    print('-----------------')
