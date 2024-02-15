import random


kleuren = ("rood", "geel", "blauw", "groen", "bruin", "oranje")


aantal = int(input("Hoeveel M&M's wil je toevoegen? "))


bagofmnms = {

}

for i in range(aantal):
    kleur_random = random.choice(kleuren)
    if kleur_random not in bagofmnms:
        bagofmnms[kleur_random] = 0
    bagofmnms[kleur_random] +=1  


print(bagofmnms)