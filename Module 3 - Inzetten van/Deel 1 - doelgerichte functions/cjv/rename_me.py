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

def is_getal_even(getal:int) -> bool:
    return getal % 2 == 0

def woorden_omkeren(zin:str) -> str:
    split_word = zin.split()
    volgorde_omkeren = split_word[::-1]
    maak_string = ' '.join(volgorde_omkeren)
    return maak_string

def aantal_unieke_karakters(zin:str) -> int:
    maak_set = set(zin)
    aantal = len(maak_set)
    return aantal

def gemiddelde_lengte_woorden(zin:str) -> float:
    woorden = zin.split()
    
    getal = 0
    for lengte in woorden:
        getal += len(lengte)

    gemiddelde = getal / len(woorden)
    return gemiddelde

def tafel(tafel:int, getal:int=10) -> str:
    string = ""
    for keer in range(1, getal+1):
        som = keer * tafel
        string += f'{keer} x {tafel} = {som}\n'
    return string

# print de functie Getal_even

print(is_getal_even(4))

# print de functie omkeren

print(woorden_omkeren("Dit is een test"))

# print de functie tel_unieke_karakters

print(aantal_unieke_karakters("Dit is een test"))

# print de functie gemiddelde_lengte

print(gemiddelde_lengte_woorden("Dit is een test"))

# Test de functie tafel

print(tafel(5))