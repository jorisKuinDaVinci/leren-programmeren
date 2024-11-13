from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# Gebruik recipe_lib voor input van aantal personen
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

#Heb je dezelfde uitkomsten? Prima, dan ga je de afrondingen berekenen afhankelijk van gebruikte eenheid.
#De gebruikte eenheden van ingrediënten vind je in frittata_ingredients.py, 
# bijvoorbeeld voor melk is het UNIT_MILK = UNIT_CUPS, of voor peper is  het UNIT_PEPPER = UNIT_TEASPOONS
#Codeer in frittata1.py de afronding van hoeveelheden van alle ingrediënten afhankelijk van de hoeveelheid en van de eenheid:
#als eenheid gelijk is aan  pieces (UNIT_PIECES):
#gebruik function round_piece() in recipe_lib\
#maak die function werkend:
#meegekregen hoeveelheid (amount) naar boven afronden naar een geheel getal
#return het resultaat van de afronding
#als eenheid gelijk is aan spoons, teaspoons of cups (UNIT_SPOONS, UNIT_TEASPOONS, UNIT_CUPS):
#gebruik function round_quarter() in recipe_lib
#maak de function werkend:
#meegekregen hoeveelheid (amount) afronden naar het dichtsbijzijnde getal met: .25 of .50 of .75 of .00.
#meegekregen hoeveelheid boven de 10 afronden naar het dichtstbijzijnde gehele getal.
#return het resultaat van de afronding
#tip: kijk naar de berekening in: Real simple functions, opdracht: Afronden naar stuivers. Nu afronden naar 25 ipv 5
#Codeer het printen van de hoeveelheden de eenheden in combinatie met de omschrijving van de ingrediënten. 
#codeer het totdat de bovenstaande voorbeeld output ontstaat bij een invoer van 13 personen
#gebruik de berekenende hoeveelheden
#gebruik de TXT_ en de UNIT_ constanten in de py-code) bijvoorbeeld: TEXT_MILK of UNIT_MILK
#gebruik de typische python string formatting, bijvoorbeeld f'…….’
#nog niets doen aan het presenteren van omschrijvingen in enkelvoud of meervoud (dat komt later!)
#Test het programma voor de invoer van resp.: 1, 3, 7, 13 en 90 personen.
#Vergelijk de ouputs van de testen met de getallen in onderstaande tabel:

#personen	ei	melk	zout	peper	olie	ui	knoflook	paprika	spinazie	kaas
#1	        2	0.25	0.25	0.25	0.25	1	1	        1	    0.25	    0.25 
#3	        6	0.5	    0.5	    0.5	    0.75	1	2	        3	    0.75	    0.5 Goed
#7	        13	1.0	    1.0	    1.0	    1.75	2	4	        6	    1.75	    1.0 Goed
#13	        23	1.5	    1.5	    1.5	    3.25	4	7	        10	    3.25	    1.5 Goed
#90	        158	11	    11	    11	    22	    23	45	        68	    22	        11 Goed

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