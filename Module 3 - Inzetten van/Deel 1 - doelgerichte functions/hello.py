#define en call een function.

#Deze functie heeft een parameter waar een getal in komt.

#Als je de functie met het argument 3 aanroept dan geeft de functie 1 string terug waar in onder elkaar staat:
#Hello from function town 1!
#Hello from function town 2!
#Hello from function town 3!

#Als je de functie met het argument 7 aanroept dan geeft de functie 1 string terug waar in onder elkaar staat:
#Hello from function town 1!
#Hello from function town 2!
#Hello from function town 3!
#Hello from function town 4!
#Hello from function town 5!
#Hello from function town 6!
#Hello from function town 7!

#print de string die terug komt uit de functie (hint: hoe voeg je een enter toe aan een string?)
def hello(nummer:int) -> str:
    cijfer = 0
    tekst = ""
    for i in range(nummer):
        cijfer += 1
        tekst += "Hello from function town " + str(cijfer) + "!\n"
    return tekst

# input voor hoeveel keer de functie moet printen
nummer = input('Hoeveel keer moet de functie printen? ')
print(hello(int(nummer)))