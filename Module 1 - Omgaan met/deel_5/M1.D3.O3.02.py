from random import randint

A = randint(-1000, 1000)
B = randint(-1000, 1000)
C = randint(-1000, 1000)
D = randint(-1000, 1000)


getal = [A, B, C, D] = sorted([A, B, C, D])
kleinste = min(A, B, C, D)
grootste = max(A, B, C, D)
print(A, B, C, D)
print(max(A, B, C, D))

# Print de resultaten
print("Het kleinste getal is: ", kleinste)
print("Het grootste getal is: ", grootste)
volgorde = print("De getallen op volgorde zijn: ", getal)
omgekeerde_volgorde = print("De getallen in omgekeerde volgorde zijn: ", getal[::-1])
middelste_getallen = print("De middelste getallen zijn: ", getal[1:3])
#middelste_getal = print("Het middelste getal is: ", getal[2])