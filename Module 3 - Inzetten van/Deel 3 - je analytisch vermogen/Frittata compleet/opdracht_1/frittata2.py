from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# Gebruik recipe_lib voor input van aantal personen
nr_persons = input_nr_persons('Voor hoeveel personen wilt u frittata maken? ')

#Kan netter!
#De app geeft nu een resultaat met enkele minpuntjes.

#omschrijvingen worden getoond in enkelvoud én in meervoud, zoals “persoon|personen” of “groot ei|grote eieren” (roodomcirkeld)!  Dat is nogal twijfelachtig! We willen voor 1 ei zien: 1 groot ei. En voor 23 eieren: 23 grote eieren.
#de hoeveelheden voor lepels, theelepels en kopjes worden niet getoond zoals gebruikelijk (geelomcirkeld)! Voor bijvoorbeeld: 3.25,  1.5, 0.75 en 4.0 willen we zien: 3¼ , 1½ , ¾ en 4
#de eenheden voor lepels, theelepels en kopjes worden getoond in het Engels (groenomcirkeld)! In plaats van 1.5 teaspoon: 1½ lepel en in plaats van 3.25 cup: 3¼ kopjes. Dus Nederlandse namen en dan in enkel- of meervoud afhankelijk van de hoeveelheid. (Alles vanaf de 2 dus in meervoud!)

#Stappenplan
#Codeer in frittata2.py de enkelvoud of meervoud ingrediënt-omschrijvingen afhankelijk van de hoeveelheid.
#gebruik de function str_single_plural()
#maak de function wel eerst werkend:
#meervoud vanaf hoeveelheid 2
#hoe kan je een string splitsen in twee delen, waarvan je er een kan returnen?
#Codeer het presenteren van getallen met ¼ , ½  en ¾ (function uit recipe_lib.py?)
#gebruik de function str_amount_fraction() uit recipe_lib.py. Deze lastige function is al werkend gemaakt.
#Codeer het presenteren van de juiste eenheden voor spoons, teaspoons en cups.
#gebruik de function str_units()
#maak de function wel eerst werkend:
#maak hierin gebruik van de function str_single_prural()
#maak hierin ook gebruik van de constanten: TXT_SPOONS, TXT_TEASPOONS en TXT_CUPS
#Test de werking van frittata2 met verschillende testgevallen.

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

# calculate amount_paprikas
calc_amount_paprikas = round_piece(AMOUNT_PAPRIKAS * calc_factor)

# calculate amount_spinach
calc_amount_spinach = round_quarter(AMOUNT_SPINACH * calc_factor)

# calculate amount_cheese
calc_amount_cheese = round_quarter(AMOUNT_CHEESE * calc_factor)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f'{str_amount_fraction(calc_amount_eggs)} {str_units(calc_amount_eggs, UNIT_EGGS)} {str_single_plural(calc_amount_eggs, TXT_EGGS)}')
print(f'{str_amount_fraction(calc_amount_milk)} {str_units(calc_amount_milk, UNIT_MILK)} {TXT_MILK}')
print(f'{str_amount_fraction(calc_amount_salt)} {str_units(calc_amount_salt, UNIT_SALT)} {TXT_SALT}')
print(f'{str_amount_fraction(calc_amount_pepper)} {str_units(calc_amount_pepper, UNIT_PEPPER)} {TXT_PEPPER}')
print(f'{str_amount_fraction(calc_amount_oil)} {str_units(calc_amount_oil, UNIT_OIL)} {TXT_OIL}')
print(f'{str_amount_fraction(calc_amount_onions)} {str_units(calc_amount_onions, UNIT_ONIONS)} {str_single_plural(calc_amount_onions, TXT_ONIONS)}')
print(f'{str_amount_fraction(calc_amount_garlics)} {str_units(calc_amount_garlics, UNIT_GARLICS)} {str_single_plural(calc_amount_garlics, TXT_GARLICS)}')
print(f'{str_amount_fraction(calc_amount_paprikas)} {str_units(calc_amount_paprikas, UNIT_PAPRIKAS)} {str_single_plural(calc_amount_paprikas, TXT_PAPRIKAS)}')
print(f'{str_amount_fraction(calc_amount_spinach)} {str_units(calc_amount_spinach, UNIT_SPINACH)} {TXT_SPINACH}')
print(f'{str_amount_fraction(calc_amount_cheese)} {str_units(calc_amount_cheese, UNIT_CHEESE)} {TXT_CHEESE}')
print('-----------------------------------------------')