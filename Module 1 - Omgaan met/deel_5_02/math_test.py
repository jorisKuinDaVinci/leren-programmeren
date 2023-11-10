from math_operations import increment, decrement, add, substract, multiply, divide
from test_lib import test, report

nr1 = 3.0
nr2 = 17.0

expected = nr2 + 1 #
calculated = increment(nr2)
test('increment', expected, calculated)

expected = 29 #
calculated = increment(28)
test('extra test', expected, calculated)

expected = nr2 - 1 #
calculated = decrement(nr2)
test('decrement', expected, calculated)

expected = nr1 + nr2
calculated = add(nr1, nr2)
test('add', expected, calculated)

expected = 55
calculated = add(15, 40)
test('extra test 2', expected, calculated)

expected = 76
calculated = add(17, 59)
test('add', expected, calculated)

expected = nr2 - nr1
calculated = substract(nr2, nr1)
test('substract', expected, calculated)

expected = 34
calculated = substract(55, 21)
test('substract', expected, calculated)

expected = nr1 * nr2
calculated = multiply(nr1, nr2)
test('multiply', expected, calculated)

expected = 150
calculated = multiply(75, 2)
test('multiply', expected, calculated)

expected = nr1 / nr2
calculated = divide(nr1, nr2)
test('divide', expected, calculated)

expected = 9.0
calculated = divide(27, 3)
test('divide', expected, calculated)

expected = None
calculated = divide(nr1, 0)
test('divide by zero', expected, calculated)

report()


