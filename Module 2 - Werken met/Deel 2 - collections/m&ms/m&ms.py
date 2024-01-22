import random

kleuren = ("oranje", "blauw", "groen", "bruin")
aantal = int(input("Hoeveel M&M's wil je toevoegen? "))
zak = []
for i in range(aantal):
    zak.append(random.choice(kleuren))
print(zak)