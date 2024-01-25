list_amount = int(input("Hoeveel lijstjes wil je zien? "))
#list_length = int(input("Hoe lang moet ieder lijstje zijn? "))


for i in range(1, list_amount + 1):
    list_length = int(input("Hoe lang moet lijstje " + str(i) + " zijn? "))
    if list_length not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("Deze lijst is te lang of te kort")
        list_length = int(input("Hoe lang moet lijstje " + str(i) + " zijn? "))
    print(list(range(i, list_length + 1, i)))