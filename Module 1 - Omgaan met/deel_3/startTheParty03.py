#gastheer = True
gastheer = input("wie is de gastheer? ")
gasten = int(input("hoeveel gasten zijn er? "))
drank = True
chips = True
mij_naam = "Joris"
slb_naam = "Jouke"
gastheer_mij = gastheer == mij_naam
gastheer_slb = not gastheer == slb_naam and chips and drank
gasten_door = gasten >= 4 and gasten <= 20 and chips and drank

if (gastheer_mij or gastheer_slb) and (gasten >= 4 and gasten <= 20) and drank or chips:
    print('Start the Party')
else:
    print('No Party')