from juiste_antwoorden import JUISTE_ANTWOORDEN
from data import TEKSTEN

def vraag_invoer(prompt, opties):
    #Vraagt invoer van de gebruiker en valideert deze.
    #Blijft vragen totdat een geldige keuze is ingevoerd.
    keuze = input(prompt).strip().lower()
    while keuze not in opties:
        print(f"{TEKSTEN['keuze_ongeldig']} {', '.join(opties)}")
        keuze = input(prompt).strip().lower()
    return keuze

def controleer_antwoord(keuze, stap):
    #Controleert of de keuze overeenkomt met het juiste antwoord voor de stap.
    return keuze == JUISTE_ANTWOORDEN[stap]

def print_game_over():
    #Print de standaard 'Game over'-tekst.
    print(TEKSTEN["game_over"])

def print_introductie(naam):
    #Print een gepersonaliseerde introductie.
    print(TEKSTEN["introductie"].format(naam=naam))