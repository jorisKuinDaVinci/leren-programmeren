aantal_iteraties = 0
while True:
    antwoord = input("? ")
    aantal_iteraties += 1
    print(aantal_iteraties)
    if antwoord == "quit":
        print("Je hebt", aantal_iteraties)
        print("je hebt quit ingevoerd, het programma stopt nu.")
        break