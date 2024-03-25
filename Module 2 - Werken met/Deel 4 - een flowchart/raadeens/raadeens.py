import random

genereer_random_getal = random.randint(1, 1000)
score = 0
hoeveel_keer_geraden = 0
ronde = 0
hoeveel_getal_keer_geraden = 0
while ronde is not 20 and hoeveel_getal_keer_geraden is not 10:
    ronde += 1
    getal = int(input("Raad een getal tussen 1 en 1000: "))
    hoeveel_keer_geraden += 1
    hoeveel_getal_keer_geraden += 1
    if getal == genereer_random_getal:
        print(f"Goed geraden! Het getal was inderdaad {genereer_random_getal}")
        score += 1
        genereer_random_getal = random.randint(1, 1000)
    elif getal < genereer_random_getal:
        if abs(getal - genereer_random_getal) <= 50:
            print("Je bent warm")
        elif abs(getal - genereer_random_getal) <= 20:
            print("Je bent heel warm")
        else:
            print("Het getal is hoger")
    elif getal > genereer_random_getal:
        if abs(getal - genereer_random_getal) <= 50:
            print("Je bent warm")
        elif abs(getal - genereer_random_getal) <= 20:
            print("Je bent heel warm")
        else:
            print("Het getal is lager")
    print(f"Je hebt {score} van de {hoeveel_keer_geraden} geraden")

if hoeveel_getal_keer_geraden == 10:
    nog_een_keer = input("wil je nog een keer raden?")
    if nog_een_keer == "ja":
        hoeveel_getal_keer_geraden = 0
    else:
        print("Bedankt voor het spelen")
        exit()



