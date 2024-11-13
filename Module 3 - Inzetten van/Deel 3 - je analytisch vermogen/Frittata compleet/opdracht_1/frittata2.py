from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# Gebruik recipe_lib voor input van aantal personen
nr_persons = input_nr_persons('Voor hoeveel personen wilt u frittata maken? ')

# ----- CALCULATIONS ----
# calculate factor 
calc_factor = nr_persons / RECIPE_PERSONS  # 4 personen is de basis van het recept

# calculate amount_eggs
calc_amount_eggs = round_piece(AMOUNT_EGGS * calc_factor)

# calculate amount_milk
calc_amount_milk = round_quarter(AMOUNT_MILK * calc_factor)

# calculate amount_salt
calc_amount_salt = round_quarter(AMOUNT_SALT * calc_factor)

# calculate amount_pepper
calc_amount_pepper = round_quarter(AMOUNT_PEPPER * calc_factor)

# calculate amount_oil
calc_amount_oil = round_quarter(AMOUNT_OIL * calc_factor)

# calculate amount_onions
calc_amount_onions = round_piece(AMOUNT_ONIONS * calc_factor)

# calculate amount_garlics
calc_amount_garlics = round_piece(AMOUNT_GARLICS * calc_factor)

# calculate amount_spinach
calc_amount_spinach = round_quarter(AMOUNT_SPINACH * calc_factor)

# calculate amount_paprikas
calc_amount_paprikas = round_piece(AMOUNT_PAPRIKAS * calc_factor)

# calculate amount_cheese
calc_amount_cheese = round_quarter(AMOUNT_CHEESE * calc_factor)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f'{calc_amount_eggs} {UNIT_PIECES} {TXT_EGGS}')
print(f'{calc_amount_milk} {UNIT_CUPS} {TXT_MILK}')
print(f'{calc_amount_salt} {UNIT_TEASPOONS} {TXT_SALT}')
print(f'{calc_amount_pepper} {UNIT_TEASPOONS} {TXT_PEPPER}')
print(f'{calc_amount_oil} {UNIT_SPOONS} {TXT_OIL}')
print(f'{calc_amount_onions} {UNIT_PIECES} {TXT_ONIONS}')
print(f'{calc_amount_garlics} {UNIT_PIECES} {TXT_GARLICS}')
print(f'{calc_amount_spinach} {UNIT_CUPS} {TXT_SPINACH}')
print(f'{calc_amount_paprikas} {UNIT_PIECES} {TXT_PAPRIKAS}')
print(f'{calc_amount_cheese} {UNIT_CUPS} {TXT_CHEESE}')
print('-----------------------------------------------')