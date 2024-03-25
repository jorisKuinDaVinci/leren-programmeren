import random

random_getal = random.randint(1, 1000)
print(random_getal) # voor testen
score = 0
hoeveel_keer_geraden = 0
ronde = 0
hoeveel_getal_keer_geraden = 0
while ronde != 20:
    ronde += 1
    while hoeveel_getal_keer_geraden != 10:
        getal = int(input("Raad een getal tussen 1 en 1000: "))
        hoeveel_keer_geraden += 1
        hoeveel_getal_keer_geraden += 1
        if getal == random_getal:
            print(f"Goed geraden! Het getal was inderdaad {random_getal}")
            score += 1
            random_getal = random.randint(1, 1000)
            print(random_getal) # voor testen
            break
        elif getal < random_getal:
            if abs(getal - random_getal) <= 50:
                print("Je bent warm")
            elif abs(getal - random_getal) <= 20:
                print("Je bent heel warm")
            else:
                print("Het getal is hoger")
        elif getal > random_getal:
            if abs(getal - random_getal) <= 50:
                print("Je bent koud")
            elif abs(getal - random_getal) <= 20:
                print("Je bent heel koud")
            else:
                print("Het getal is lager")
        print(f"Je hebt {score} van de {hoeveel_keer_geraden} geraden")
        doorgaan = print(input("Wil je doorgaan? ja of nee: "))
        if doorgaan == "nee":
            break
        elif doorgaan == "ja":
            continue

    if hoeveel_getal_keer_geraden == 10:
        nog_een_keer = input("wil je nog een keer raden? ja of nee:")
        if nog_een_keer == "ja":
            hoeveel_getal_keer_geraden = 0
        else:
            print("Bedankt voor het spelen")
            exit()

    if ronde == 20:
        print("Het spel is afgelopen")
        print(f"Je hebt {score} van de 20 geraden")
        nog_een_keer_spelen = input("wil je nog een keer het spel spelen? ja of nee: ")
        if nog_een_keer_spelen == "ja":
            ronde = 0
            score = 0
            hoeveel_getal_keer_geraden = 0
            random_getal = random.randint(1, 1000)
            print(random_getal) # voor testen
        else:
            print("Bedankt voor het spelen")
            exit()



