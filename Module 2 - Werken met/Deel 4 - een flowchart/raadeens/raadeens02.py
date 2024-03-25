import random

score = 0
ronde = 0

while ronde != 20:
    ronde += 1
    hoeveel_keer_geraden = 0
    random_getal = random.randint(1, 1000)
    print(random_getal)  # voor testen
    while hoeveel_keer_geraden != 10:
        getal = int(input("Raad een getal tussen 1 en 1000: "))
        hoeveel_keer_geraden += 1
        if getal == random_getal:
            print(f"Goed geraden! Het getal was inderdaad {random_getal}")
            score += 1
            print(f"Je hebt {score} van de {hoeveel_keer_geraden} geraden")
            goed_geraden = True
        else:
            if abs(getal - random_getal) <= 20:
                print("Je bent heel warm")
            elif abs(getal - random_getal) <= 50:
                print("Je bent warm")
            else:
                print("je bent koud")
            if getal < random_getal:
                print("Het getal is hoger")
            else:
                print("Het getal is lager")    
            print(f"Je hebt {score} van de {hoeveel_keer_geraden} geraden")
            doorgaan = input("Wil je doorgaan? ja of nee: ").lower()
            if doorgaan == "nee":
                exit()

        if hoeveel_keer_geraden == 10 or goed_geraden == True:
            nog_een_keer = input("Wil je nog een keer raden? ja of nee:").lower()
            if nog_een_keer == "ja":
                continue
            else:
                print("Bedankt voor het spelen")
                exit()

    if ronde == 20:
        print("Het spel is afgelopen")
        print(f"Je hebt {score} van de 20 geraden")
        nog_een_keer_spelen = input("Wil je nog een keer het spel spelen? ja of nee: ").lower()
        if nog_een_keer_spelen == "ja":
            ronde = 0
            score = 0
        else:
            print("Bedankt voor het spelen")
            exit()