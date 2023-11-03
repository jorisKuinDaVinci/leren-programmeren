from math_operations import increment, decrement, add, substract, multiply, divide
from test_lib import test, report
#Je hebt voor de opdracht 'M1.D3.O1 - Meten is weten’ een keer code geschreven die print welk getal van twee getallen het grootste is.
# Nu ga je daar een function van maken met 2 parameters voor de te vergelijken getallen die een string teruggeeft.
# Definieer een function:
# met een duidelijke naam en alle type aanduidingen
# Met 2 parameters voor twee int getallen: nr1 en nr2
# Returnt de string: 'Beide getallen zijn even groot’, als nr1 en nr2 even groot blijken te zijn
# Returnt de string: f'Maximum: {nr1} en minimum: {nr2}’ als nr1 groter is
# Returnt de string: f'Maximum: {nr2} en minimum: {nr1}’ als nr2 groter is
# Test voor de 3 gevallen! Gebruik test_lib.py
# Maak een report met report() en lever die in bij je docent.
# Test je code met de test_lib.py

def grootste_getal(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    elif nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
    else:
        return 'Beide getallen zijn even groot'
nr1 = 3
nr2 = 11
nr3 = 37
nr4 = 79
result1 = grootste_getal(nr1, nr2)
result2 = f'Maximum: {nr2} en minimum: {nr1}'
test('grootste_getal', result1, result2)
result3 = grootste_getal(nr3, nr4)
result4 = f'Maximum: {nr4} en minimum: {nr3}'
test('grootste_getal', result3, result4)
result5 = grootste_getal(nr1, nr1)
report()

   