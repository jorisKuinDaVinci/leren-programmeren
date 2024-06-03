tafel = 1
for _ in range(1, 101):
    for tafel in range(1, 101):
        print("")
        print(f"tafel van {tafel}: ")
        for cijfer in range(1, 11):
            print(f"{cijfer} x {tafel} = {cijfer * tafel}")      