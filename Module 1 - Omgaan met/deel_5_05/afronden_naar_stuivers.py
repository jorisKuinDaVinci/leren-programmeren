from test_lib import test, report
# Hier is de code van de slimme vakkenvuller:

print('voorbeelden van gewenste afrondingen afronden naar 5 cents munten')
print('€62.60 afronden naar €', round(62.60 * 100 / 5) * 5 / 100)
print('€76.61 afronden naar €', round(76.61 * 100 / 5) * 5 / 100)
print('€ 28.82 afronden naar €', round(28.82 * 100 / 5) * 5 / 100)
print('€ 2.23 afronden naar €', round(2.23 * 100 / 5) * 5 / 100)
print('€ 28.34 afronden naar €', round(28.34 * 100 / 5) * 5 / 100)
print('€ -42.85 afronden naar €', round(-42.85 * 100 / 5) * 5 / 100)
print('€ 31.06 afronden naar €', round(31.06 * 100 / 5) * 5 / 100)
print('€ -138.47 afronden naar €', round(-138.47 * 100 / 5) * 5 / 100)
print('€ 14.88 afronden naar €', round(14.88 * 100 / 5) * 5 / 100)
print('€ 149.69 afronden naar €', round(149.69 * 100 / 5) * 5 / 100)
print('LETOP: In de toekomst ook afronden op 10 cents of 20 cents munten')

#Opdracht:

def round_to_5_cents(amount):
    return round(amount * 100 / 5) * 5 / 100

amount = 62.60
expect_rounded_amount = 62.60
rounded_amount = round_to_5_cents(amount)
name = f'test amount: {amount}'
test(name, expect_rounded_amount, rounded_amount )

report()

amount = 76.61
expect_rounded_amount = 76.60
rounded_amount = round_to_5_cents(amount)
name = f'test amount: {amount}'
test(name, expect_rounded_amount, rounded_amount )

report()

amount = 28.82
expect_rounded_amount = 28.80
rounded_amount = round_to_5_cents(amount)
name = f'test amount: {amount}'
test(name, expect_rounded_amount, rounded_amount )

report()

amount = 2.23
expect_rounded_amount = 2.25
rounded_amount = round_to_5_cents(amount)
name = f'test amount: {amount}'
test(name, expect_rounded_amount, rounded_amount )

report()

amount = 28.34
expect_rounded_amount = 28.35
rounded_amount = round_to_5_cents(amount)
name = f'test amount: {amount}'
test(name, expect_rounded_amount, rounded_amount )

report()