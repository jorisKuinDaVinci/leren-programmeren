list_amount = int(input("Hoeveel lijstjes wil je zien? "))
list_length = int(input("Hoe lang moet ieder lijstje zijn? "))
for i in range(1, list_amount + 1):
    print(list(range(i, list_length + 1, i)))