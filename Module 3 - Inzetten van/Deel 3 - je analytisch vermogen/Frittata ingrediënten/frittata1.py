from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('Voor hoeveel personen wilt u frittata maken? ')

# ----- CALCULATIONS ----
# calculate factor 
calc_factor = nr_persons / 4 # 4 persons is the base of the recipe

# calculate amount_eggs
calc_amount_eggs = round_piece(4 * calc_factor)

# calculate amount_milk
calc_amount_milk = round_quarter(0.5 * calc_factor)

# calculate amount_salt
calc_amount_salt = round_quarter(0.5 * calc_factor)

# calculate amount_pepper
calc_amount_pepper = round_quarter(0.5 * calc_factor)

# calculate amount_oil
calc_amount_oil = round_quarter(1 * calc_factor)

# calculate amount_onions
calc_amount_onions = round_quarter(1 * calc_factor)

# calculate amount_garlics
calc_amount_garlics = round_quarter(1 * calc_factor)

# calculate amount_spinach
calc_amount_spinach = round_quarter(400 * calc_factor)

# calculate amount_paprikas
calc_amount_paprikas = round_quarter(2 * calc_factor)

# calculate amount_cheese
calc_amount_cheese = round_quarter(100 * calc_factor)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f'{calc_amount_eggs} {str_units(calc_amount_eggs, UNIT_PIECES)}')
print(f'{calc_amount_milk} {str_units(calc_amount_milk, UNIT_CUPS)}')
print(f'{calc_amount_salt} {str_units(calc_amount_salt, UNIT_TEASPOONS)}')
print(f'{calc_amount_pepper} {str_units(calc_amount_pepper, UNIT_TEASPOONS)}')
print(f'{calc_amount_oil} {str_units(calc_amount_oil, UNIT_SPOONS)}')
print(f'{calc_amount_onions} {str_units(calc_amount_onions, UNIT_PIECES)}')
print(f'{calc_amount_garlics} {str_units(calc_amount_garlics, UNIT_PIECES)}')
print(f'{calc_amount_spinach} {str_units(calc_amount_spinach, UNIT_CUPS)}')
print(f'{calc_amount_paprikas} {str_units(calc_amount_paprikas, UNIT_PIECES)}')
print(f'{calc_amount_cheese} {str_units(calc_amount_cheese, UNIT_CUPS)}')
print('-----------------------------------------------')