som = 0
while True:
    antwoord = input("quit of getal: ")
    if antwoord == "quit":
        print("je hebt quit ingevoerd, het programma stopt nu.")
        break
    som += int(antwoord)

print(som)