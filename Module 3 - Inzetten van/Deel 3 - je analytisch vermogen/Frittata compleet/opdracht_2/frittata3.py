from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# Gebruik recipe_lib voor input van aantal personen
nr_persons = input_nr_persons('Voor hoeveel personen wilt u frittata maken? ')

#Stappenplan
#Codeer de berekening van het volume in ml van alle ingrediënten met lepels, theelepels en kopjes. Niet stuks!
#gebruik de function in unit2ml() uit recipe_lib.py
#maak de function wel eerst werkend.
#reken daarin het aantal eenheden (amount) om naar ml
#3 lepels is bijvoorbeeld gelijk aan 45 ml
#gebruik daarin de constanten: ML_SPOON, ML_TEASPOON en ML_CUP
#genereer een TypeError als een unit is meegegeven anders dan: UNIT_SPOONS, UNIT_TEASPOONS of UNIT_CUPS
#return het resultaat (in ml)
#Codeer de berekening van het gewicht in gram op basis van het volume voor zout, peper, spinazie en kaas. Daarvoor is het soortelijk gewicht (gram per ml) nodig van die ingrediënten.
#gebruik de function ml2gram()
#maak de function wel eerst werkend:
#reken daarin het aantal ml (amount_ml) om naar gram.
#10 ml zout is bijvoorbeeld gelijk aan 12 gram.
#gebruik de constanten: GRAM_PER_ML_SALT, GRAM_PER_ML_PEPPER, GRAM_PER_ML_CHEESE, GRAM_PER_ML_SPINACH
#return het resultaat (in gram)
#Codeer het printen van het volume en gewicht van ingrediënten
#zoals in voorbeeld
#tot 100 met één decimaal nauwkeurigheid.
#vanaf 100 met nul decimalen nauwkeurigheid.
#Test de werking.

# ----- CALCULATIONS ----
# calculate factor 
calc_factor = nr_persons / RECIPE_PERSONS  # 4 personen is de basis van het recept

# calculate amount_eggs
calc_amount_eggs = round_piece(AMOUNT_EGGS * calc_factor)

# calculate amount_milk
calc_amount_milk = round_quarter(AMOUNT_MILK * calc_factor)
volume_milk_ml = unit2ml(calc_amount_milk, UNIT_CUPS)

# calculate amount_salt
calc_amount_salt = round_quarter(AMOUNT_SALT * calc_factor)
volume_salt_ml = unit2ml(calc_amount_salt, UNIT_TEASPOONS)
weight_salt_g = ml2gram(volume_salt_ml, GRAM_PER_ML_SALT)

# calculate amount_pepper
calc_amount_pepper = round_quarter(AMOUNT_PEPPER * calc_factor)
volume_pepper_ml = unit2ml(calc_amount_pepper, UNIT_TEASPOONS)
weight_pepper_g = ml2gram(volume_pepper_ml, GRAM_PER_ML_PEPPER)

# calculate amount_oil
calc_amount_oil = round_quarter(AMOUNT_OIL * calc_factor)
volume_oil_ml = unit2ml(calc_amount_oil, UNIT_SPOONS)

# calculate amount_onions
calc_amount_onions = round_piece(AMOUNT_ONIONS * calc_factor)

# calculate amount_garlics
calc_amount_garlics = round_piece(AMOUNT_GARLICS * calc_factor)

# calculate amount_paprikas
calc_amount_paprikas = round_piece(AMOUNT_PAPRIKAS * calc_factor)

# calculate amount_spinach
calc_amount_spinach = round_quarter(AMOUNT_SPINACH * calc_factor)
volume_spinach_ml = unit2ml(calc_amount_spinach, UNIT_CUPS)
weight_spinach_g = ml2gram(volume_spinach_ml, GRAM_PER_ML_SPINACH)

# calculate amount_cheese
calc_amount_cheese = round_quarter(AMOUNT_CHEESE * calc_factor)
volume_cheese_ml = unit2ml(calc_amount_cheese, UNIT_CUPS)
weight_cheese_g = ml2gram(volume_cheese_ml, GRAM_PER_ML_CHEESE)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f"{str_amount_fraction(calc_amount_eggs)} {str_units(calc_amount_eggs, UNIT_EGGS)} {str_single_plural(calc_amount_eggs, TXT_EGGS)}")
print(f"{str_amount_fraction(calc_amount_milk)} {str_units(calc_amount_milk, UNIT_CUPS)} {TXT_MILK} ({volume_milk_ml:.1f} ml)")
print(f"{str_amount_fraction(calc_amount_salt)} {str_units(calc_amount_salt, UNIT_TEASPOONS)} {TXT_SALT} ({volume_salt_ml:.1f} ml, {weight_salt_g:.1f} g)")
print(f"{str_amount_fraction(calc_amount_pepper)} {str_units(calc_amount_pepper, UNIT_TEASPOONS)} {TXT_PEPPER} ({volume_pepper_ml:.1f} ml, {weight_pepper_g:.1f} g)")
print(f"{str_amount_fraction(calc_amount_oil)} {str_units(calc_amount_oil, UNIT_SPOONS)} {TXT_OIL} ({volume_oil_ml:.1f} ml)")
print(f"{str_amount_fraction(calc_amount_onions)} {str_units(calc_amount_onions, UNIT_PIECES)} {str_single_plural(calc_amount_onions, TXT_ONIONS)}")
print(f"{str_amount_fraction(calc_amount_garlics)} {str_units(calc_amount_garlics, UNIT_PIECES)} {str_single_plural(calc_amount_garlics, TXT_GARLICS)}")
print(f"{str_amount_fraction(calc_amount_paprikas)} {str_units(calc_amount_paprikas, UNIT_PIECES)} {str_single_plural(calc_amount_paprikas, TXT_PAPRIKAS)}")
print(f"{str_amount_fraction(calc_amount_spinach)} {str_units(calc_amount_spinach, UNIT_CUPS)} {TXT_SPINACH} ({volume_spinach_ml:.1f} ml, {weight_spinach_g:.1f} g)")
print(f"{str_amount_fraction(calc_amount_cheese)} {str_units(calc_amount_cheese, UNIT_CUPS)} {TXT_CHEESE} ({volume_cheese_ml:.1f} ml, {weight_cheese_g:.1f} g)")
print('-----------------------------------------------')