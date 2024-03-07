totale_som = 0
current_cijfer = 50
iteration = 1

while totale_som <= 1000:
    totale_som += current_cijfer
    print(f"{iteration}. ", end="")
    
    for cijfer in range(50, current_cijfer + 1):
        if cijfer != current_cijfer:
            print(f"{cijfer} + ", end="")
        else:
            print(cijfer, end="")
    
    print(f" = {totale_som}")
    
    current_cijfer += 1
    iteration += 1
