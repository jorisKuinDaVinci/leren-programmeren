tafel = 1
for tafel in range(1, 3):
    print("")
    print(f"tafel van {tafel}: ")
    for cijfer in range(1, 11):
        print(f"{cijfer} x {tafel} = {cijfer * tafel}")      

# print onder elkaar alle cijfers van 99 t/m 215.
# print onder elkaar 25 keer ik ben geweldig.
# print onder elkaar ik vindt dit niet zo leuk.
# print 25 keer onder elkaar ik ben geweldig met direct daaronder ik vindt dit saai worden.
cijfer = 98
for i in range(99, 216, 1):
    cijfer += 1
    print(cijfer)
for i in range(25):
    print("ik ben geweldig")
for i in range(25):
    print("ik vindt dit niet zo leuk")
for geweldig in range(25):
    print("ik ben geweldig") 
    geweldig += 1
    if geweldig == 25:
        print("ik vindt dit saai worden")