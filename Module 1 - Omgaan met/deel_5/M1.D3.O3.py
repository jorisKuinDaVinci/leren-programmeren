from random import randint

A = randint(-1000, 1000)
B = randint(-1000, 1000)
C = randint(-1000, 1000)
D = randint(-1000, 1000)

# bouw hier je nested if
if A < B:
    if A < C:
        if A < D:
            if B > C:
                if B > D:
                    if C < D:
                        print("getal A", A, "is wat het is, getal C", C, "is groter, getal D", D, "is nog groter, maar getal B", B, "is het grootst!")
                    else:
                        if D < C:
                            if B > D:
                                if D > A:
                                    print("getal A", A, "is wat het is, getal D", D, "is groter, getal B", B, "is nog groter, maar getal C", C, "is het grootst!")
                                else:
                                    print(A)
                            else:
                                print(D)
                        else:
                            if C > D:
                                print(C)
                            else:
                                print(D)

