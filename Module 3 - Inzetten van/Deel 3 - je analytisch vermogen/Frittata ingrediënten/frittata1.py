from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('Voor hoeveel personen wilt u frittata maken? ')
# Tijd voor een test
# bij een invoer van 13 personen, de berekening moet dan opleveren:
# eggs: 22.75; 
# milk: 1.625; 
# salt: 1.625; 
# pepper: 1.625; 
# oil: 3.25; 
# onions: 3.25; 
# garlics: 6.5; 
# paprikas: 3.25; 
# spinach: 9.75; 
# cheese: 1.625

# bij een invoer van 90 personen, de berekening moet opleveren::
# eggs: 157.5; 
# milk: 11.25; 
# salt: 11.25; 
# pepper: 11.25; 
# oil: 22.5; 
# onions: 22.5; 
# garlics: 45; 
# paprikas: 22.5; 
# spinach: 67.5; 
# cheese: 11.25

# ----- CALCULATIONS ----
# calculate factor 
calc_factor = nr_persons / 4 # 4 persons is the base of the recipe

# calculate amount_eggs
calc_amount_eggs = AMOUNT_EGGS * calc_factor

# calculate amount_milk
calc_amount_milk = AMOUNT_MILK * calc_factor

# calculate amount_salt
calc_amount_salt = AMOUNT_SALT * calc_factor

# calculate amount_pepper
calc_amount_pepper = AMOUNT_PEPPER * calc_factor

# calculate amount_oil
calc_amount_oil = AMOUNT_OIL * calc_factor

# calculate amount_onions
calc_amount_onions = AMOUNT_ONIONS * calc_factor

# calculate amount_garlics
calc_amount_garlics = AMOUNT_GARLICS * calc_factor

# calculate amount_spinach
calc_amount_spinach = AMOUNT_SPINACH * calc_factor

# calculate amount_paprikas
calc_amount_paprikas = AMOUNT_PAPRIKAS * calc_factor

# calculate amount_cheese
calc_amount_cheese = AMOUNT_CHEESE * calc_factor

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f'{calc_amount_eggs} {UNIT_EGGS} {TXT_EGGS}')
print(f'{calc_amount_milk} {UNIT_MILK} {TXT_MILK}')
print(f'{calc_amount_salt} {UNIT_SALT} {TXT_SALT}')
print(f'{calc_amount_pepper} {UNIT_PEPPER} {TXT_PEPPER}')
print(f'{calc_amount_oil} {UNIT_OIL} {TXT_OIL}')
print(f'{calc_amount_onions} {UNIT_ONIONS} {TXT_ONIONS}')
print(f'{calc_amount_garlics} {UNIT_GARLICS} {TXT_GARLICS}')
print(f'{calc_amount_spinach} {UNIT_SPINACH} {TXT_SPINACH}')
print(f'{calc_amount_paprikas} {UNIT_PAPRIKAS} {TXT_PAPRIKAS}')
print(f'{calc_amount_cheese} {UNIT_CHEESE} {TXT_CHEESE}')
print('-----------------------------------------------')