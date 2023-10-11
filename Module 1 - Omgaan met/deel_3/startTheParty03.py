#gastheer = True
gastheer = input("wie is de gastheer? ")
gasten = int(input("hoeveel gasten zijn er? "))
drank = True
chips = True

if gastheer == "Joris" and gasten >= 4 and drank and chips:
    print('Start the Party')
else:
    print('No Party')