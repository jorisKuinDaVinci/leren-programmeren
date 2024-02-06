import random


kleuren = ("rood", "geel", "blauw", "groen", "bruin")


aantal = int(input("Hoeveel M&M's wil je toevoegen? "))


bagofmnms = {
    "rood": 0,
    "geel": 0,
    "blauw": 0,
    "groen": 0,
    "bruin": 0

}


for i in range(aantal):
    bagofmnms[random.choice(kleuren)] += 1


print(bagofmnms)