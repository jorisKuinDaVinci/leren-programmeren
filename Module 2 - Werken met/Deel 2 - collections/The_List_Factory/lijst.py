from string import ascii_lowercase
print(ascii_lowercase)
print(ascii_lowercase[1:5:2])

input_lijst = input("Hoeveel lijstjes wil je? ")
input_lijst = int(input_lijst)
lijst = []
for i in range(input_lijst):
    input_letters = input("Hoeveel letters wil je in lijstje " + str(i + 1) + "? ")
    input_letters = int(input_letters)
    lijst.append([])
    for j in range(input_letters):
        input_letter = input("Geef letter " + str(j + 1) + " van lijstje " + str(i + 1) + ": ")
        lijst[i].append(input_letter)
print(lijst)
print(ascii_lowercase(lijst[0]))