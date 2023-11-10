from test_lib import test, report

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

   