from test_lib import test, report

def grootste_getal(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    elif nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
    else:
        return 'Beide getallen zijn even groot'


expected = f'Beide getallen zijn even groot'
calculated = grootste_getal(5, 5)
test('grootste_getal', expected, calculated)

report() 