cijfer = 50
som = 0
aantal_iteraties = 0
while som <= 1000:
    som += cijfer
    aantal_iteraties += 1
    print("aantal iteraties = ", aantal_iteraties, ",", "cijfer = ", cijfer, ",", "som = ", som)
    cijfer += 1
    if som >= 1000:
        print("De som is hoger dan 1000")
        break