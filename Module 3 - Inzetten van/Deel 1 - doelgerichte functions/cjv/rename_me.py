# wat doet Getal_even?
# Getal_even is een functie die een integer als input krijgt en kijkt of het getal even is. 
# Als het getal even is, dan geeft de functie True terug, anders False.

# wat doet omkeren?
# omkeren is een functie die een string als input krijgt en de woorden in de string omkeert. 
# De functie split de string in woorden, keert de volgorde van de woorden om en voegt de woorden weer samen tot een string. 
# Deze string wordt vervolgens teruggegeven.

# wat doet tel_unieke_karakters?
# tel_unieke_karakters is een functie die een string als input krijgt en de unieke karakters in de string telt.
# De functie maakt een set van de karakters in de string en telt het aantal elementen in de set.

# wat doet gemiddelde_lengte?
# gemiddelde_lengte is een functie die een string als input krijgt en de gemiddelde lengte van de woorden in de string berekent.
# De functie split de string in woorden en telt de lengte van elk woord.
# De functie berekent het gemiddelde van de lengte van de woorden en geeft dit terug.

# wat doet keer?
# keer is een functie die twee integers als input krijgt en een for loop uitvoert.
# In de for loop wordt de eerste integer vermenigvuldigd met de iteratie van de loop en het resultaat wordt geprint.

def Getal_even(integer_1:int) -> bool:
    return integer_1 % 2 == 0

def omkeren(string_1:str) -> str:
    split_word = string_1.split()
    volgorde_omkeren = split_word[::-1]
    maak_string = ' '.join(volgorde_omkeren)
    return maak_string

def tel_unieke_karakters(string_2:str) -> int:
    maak_set = set(string_2)
    aantal = len(maak_set)
    return aantal

def gemiddelde_lengte(string_3:str) -> float:
    split_word_2 = string_3.split()
    
    getal = 0
    for lengte in split_word_2:
        getal += len(lengte)

    gemiddelde = getal / len(split_word_2)
    return gemiddelde

def tafel(integer_2:int, integer_3:int=10) -> str:
    tafel_string = ""
    for for_loop_vermenigvuldigd in range(1, integer_3+1):
        vermenigvuldigd_1 = for_loop_vermenigvuldigd * integer_2
        tafel_string += f'{for_loop_vermenigvuldigd} x {integer_2} = {vermenigvuldigd_1}\n'
        #print(f'{for_loop_vermenigvuldigd} x {integer_2} = {vermenigvuldigd_1}')
    return tafel_string

# print de functie Getal_even

print(Getal_even(4))

# print de functie omkeren

print(omkeren("Dit is een test"))

# print de functie tel_unieke_karakters

print(tel_unieke_karakters("Dit is een test"))

# print de functie gemiddelde_lengte

print(gemiddelde_lengte("Dit is een test"))

# Test de functie tafel

print(tafel(5))