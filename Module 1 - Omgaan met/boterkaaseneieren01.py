from user_input import * #get_integer

# vraagt de gebruiker de gewenste plek.
#
def get_position() -> str:
    position = 0
    while position < 11 or position > 33:
        position = get_integer("Kies een vakje tussen 11 en 33:")
        #print("Kies een waarde tussen 11 en 33")

    return str(position)


# het spelletje boter, kaas en eieren

rij_1 = ['U', 'U', 'U']
rij_2 = ['U', 'U', 'U']
rij_3 = ['U', 'U', 'U']

print(rij_1)
print(rij_2)
print(rij_3)

# move speler 1 - X
move = get_position() # we krijgen '11' terug
print(move)
print(move[0])