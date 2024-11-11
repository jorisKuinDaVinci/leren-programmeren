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


# calculate amount_milk


# calculate amount_salt


# calculate amount_pepper


# calculate amount_oil


# calculate amount_onions


# calculate amount_garlics


# calculate amount_spinach


# calculate amount_paprikas


# calculate amount_cheese


# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print('-----------------------------------------------')