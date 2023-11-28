
def bereken_ik_aantal(tekst: str): # in de functiedef. heet txt een parameter. Bij de aanroep spreek je over een argument!
    aantal = 0 # variabele aantal wordt geïnitialiseerd met waarde 0
    tekst = tekst.lower() # verander uppercase characters naar lowercase
    woorden = tekst.split(' ') # split tekst in woorden
    for woord in woorden: # herhaal voor elk woord in een list woorden
        if woord in ('ik','mijn'): # woord equal to ik?
            aantal += 1 # aantal = aantal + 1
    return aantal # return aantal



tekst = """Ik ben een geweldige programmeur, mijn skils zijn huizenhoog. """

print(bereken_ik_aantal(tekst)) # hier heet het dus een argument!