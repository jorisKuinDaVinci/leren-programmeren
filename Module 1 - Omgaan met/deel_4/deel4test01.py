def vraag_getal(aantal):
    antwoord = input("Voer het "+aantal+" getal in: ")
    try:
        getal = int(antwoord)
    except ValueError:
        print("Voer cijvers in!")
        
            
    return getal


getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")