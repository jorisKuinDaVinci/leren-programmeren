def string_to_woordenlijst(zin: str)-> [str]: # in de functiedef. heet txt een parameter. Bij de aanroep spreek je over een argument!
    tekst = zin.lower() # verander uppercase characters naar lowercase
    print(tekst)
    woorden = tekst.split(' ') # split tekst in woorden
    print(woorden)
    return woorden # return aantal
def bereken_ik_aantal(tekst: str): # in de functiedef. heet txt een parameter. Bij de aanroep spreek je over een argument!
    aantal = 0 # variabele aantal wordt waarde 0
    
    woordenlijst = string_to_woordenlijst(tekst)
    for woord in woordenlijst: # herhaal voor elk woord in een list woorden
        if woord == 'ik': # woord equal to ik?
            aantal += 1
    return aantal # return aantal



tekst = """Ik ben een geweldige programmeur, mijn skils zijn huizenhoog. """

print(bereken_ik_aantal(tekst)) # hier heet het dus een argument!