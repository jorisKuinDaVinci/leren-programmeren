from random import randint

A = randint(-1000, 1000)
B = randint(-1000, 1000)
C = randint(-1000, 1000)
D = randint(-1000, 1000)


lijst_org = [A, B, C, D]
zin = 'ABCD'
kleinste = min(A, B, C, D)
grootste = max(A, B, C, D)
print(A, B, C, D)
print(max(A, B, C, D))

# Print de resultaten
print("Het kleinste getal is: ", kleinste)
print("Het grootste getal is: ", grootste)
lijst = sorted(lijst_org[::])
#print(f"({lijst[0]}) is wat het is")
print(lijst)
print(f"getal {zin[lijst_org.index({lijst[0]})]} is wat het is, getal {zin[lijst_org.index({lijst[1]})]} is groter, getal {zin[lijst_org.index({lijst[2]})]} is nog groter, maar getal {zin[lijst_org.index({lijst[3]})]} is het grootst!")
