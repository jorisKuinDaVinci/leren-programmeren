import random

# Genereer 4 willekeurige getallen tussen -1000 en 1000
A = random.randint(-1000, 1000)
B = random.randint(-1000, 1000)
C = random.randint(-1000, 1000)
D = random.randint(-1000, 1000)

# Bepaal de volgorde van de constanten volgens hun grootte
kleinste = min(A, B, C, D)
grootste = max(A, B, C, D)

# Print de resultaten
print(f"Getal A ({A}) is wat het is,", end=' ')
if A < B:
    print(f"getal B ({B}) is groter,", end=' ')
if A < C:
    print(f"getal C ({C}) is groter,", end=' ')
if A < D:
    print(f"getal D ({D}) is groter,", end=' ')
if A == grootste:
    print("en getal A is het grootst!")
else:
    print()

print(f"Getal B ({B}) is wat het is,", end=' ')
if B < A:
    print(f"getal A ({A}) is groter,", end=' ')
if B < C:
    print(f"getal C ({C}) is groter,", end=' ')
if B < D:
    print(f"getal D ({D}) is groter,", end=' ')
if B == grootste:
    print("en getal B is het grootst!")
else:
    print()

print(f"Getal C ({C}) is wat het is,", end=' ')
if C < A:
    print(f"getal A ({A}) is groter,", end=' ')
if C < B:
    print(f"getal B ({B}) is groter,", end=' ')
if C < D:
    print(f"getal D ({D}) is groter,", end=' ')
if C == grootste:
    print("en getal C is het grootst!")
else:
    print()

print(f"Getal D ({D}) is wat het is,", end=' ')
if D < A:
    print(f"getal A ({A}) is groter,", end=' ')
if D < B:
    print(f"getal B ({B}) is groter,", end=' ')
if D < C:
    print(f"getal C ({C}) is groter,", end=' ')
if D == grootste:
    print("en getal D is het grootst!")
else:
    print()
