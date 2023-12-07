from random import shuffle, choice
from time import sleep

DIEREN = ['Giraffe', 'Zebra', 'Struisvogel', 'Gazelle', 'Emoe']
dieren_lijst = [] # lege list
dieren_teller = {} # lege dict

# maak nu de savanne!
for _ in range(75):
    dieren_lijst.append(choice(DIEREN))

for _ in range(3):
    dieren_lijst.append('Neushoorn')

# vervolgens tellen we de dieren.
for dier in dieren_lijst:
    print(dier)
    if dier in dieren_teller:
        dieren_teller[dier] += 1
    else:
        dieren_teller[dier] = 1
        #print(dieren_teller) 
        #time.sleep(2)

#print(dieren_teller)    

# en vragen we of het aantal dieren klopt! 
for dier, aantal in dieren_teller.items():
#for dier in dieren_teller.keys(): 
#for aantal in dieren_teller.values():  
    if input(f"Er zijn {aantal} {dier}, klopt dit? (ja/ nee)") == 'nee': 
        print(f'Tel dan nu zelf de: {dier}')
        dieren_teller[dier] = int(input(f'Hoeveel heb je er?'))  
    #print(dier)
    #print(aantal)

# print nu een rapportje met het aantal dieren per soort:
totaal = 0
print('Rapport savanne:')
for dier, aantal in dieren_teller.items():
    print(f'{dier}: {aantal}')
    totaal += aantal
print(f'Totaal: {totaal}')