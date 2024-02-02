list_amount = int(input("Hoeveel lijstjes wil je zien? "))
lijst_leeg = []

for i in range(1, list_amount + 1):
    lijst_hoeveel_getallen = int(input("Hoeveel getallen moet lijstje " + str(i) + " hebben? "))
    while lijst_hoeveel_getallen not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("Deze lijst is te lang of te kort")
        lijst_hoeveel_getallen = int(input("Hoeveel getallen moet lijstje " + str(i) + " hebben? "))
    lijst = (list(range(i, lijst_hoeveel_getallen * i + 1, i)))    
    print(lijst)
    lijst_leeg.append(lijst)

print(lijst_leeg)