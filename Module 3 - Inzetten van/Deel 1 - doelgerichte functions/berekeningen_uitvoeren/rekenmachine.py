from functions_bestand import *

def pak_nummers(single=False):
    """Vraagt om input van de gebruiker. Als single True is, wordt alleen n1 gevraagd."""
    n1 = float(input("Voer het eerste getal in: "))
    if not single:
        n2 = float(input("Voer het tweede getal in: "))
    else:
        n2 = None
    return n1, n2

def berekennen(keuze, n1, n2=None):
    """Voert een berekening uit op basis van de keuze van de gebruiker."""
    if keuze == 'A':
        return optellen(n1, n2)
    elif keuze == 'B':
        return min(n1, n2)
    elif keuze == 'C':
        return keer(n1, n2)
    elif keuze == 'D':
        return delen(n1, n2)
    elif keuze == 'E':  # Ophogen
        return optellen(n1, 1)
    elif keuze == 'F':  # Verlagen
        return min(n1, 1)
    elif keuze == 'G':  # Verdubbelen
        return keer(n1, 2)
    elif keuze == 'H':  # Halveren
        return delen(n1, 2)
    else:
        return None

def basis_functie():
    print("Welkom bij de rekenmachine!")
    ga_door = True
    n1, n2 = None, None

    while ga_door:
        # Stap 1: Vraag de gebruiker om een keuze voor de eerste berekening
        print("Wat wilt u doen?")
        print("A) Optellen")
        print("B) Aftrekken")
        print("C) Vermenigvuldigen")
        print("D) Delen")
        print("E) Ophogen")
        print("F) Verlagen")
        print("G) Verdubbelen")
        print("H) Halveren")
        keuze = input("Maak een keuze: ").upper()

        # Stap 2: Vraag getallen (afhankelijk van keuze)
        if keuze in ['E', 'F', 'G', 'H']:
            n1, _ = pak_nummers(single=True)
        else:
            n1, n2 = pak_nummers()

        # Stap 3: Voer de berekening uit
        result = berekennen(keuze, n1, n2)
        print(f"De uitkomst is: {result}")

        # Stap 4: Vraag de gebruiker of hij verder wil met de uitkomst
        while True:
            print(f"Wil je wat met de uitkomst ({result}) doen?")
            print("A) Iets optellen")
            print("B) Iets aftrekken")
            print("C) Met iets vermenigvuldigen")
            print("D) Ergens door delen")
            print("E) Ophogen")
            print("F) Verlagen")
            print("G) Verdubbelen")
            print("H) Halveren")
            print("I) Niets (stoppen)")
            volgende_keuze = input("Maak een keuze: ").upper()

            if volgende_keuze == 'I':
                ga_door = False
                print("Bedankt voor het gebruik van de rekenmachine!")
                break
            elif volgende_keuze in ['A', 'B', 'C', 'D']:
                n2 = float(input("Voer een nieuw getal in: "))
            else:
                n2 = None

            # Stap 2-3 herhalen: gebruik de uitkomst als n1
            n1 = result
            result = berekennen(volgende_keuze, n1, n2)
            print(f"De nieuwe uitkomst is: {result}")

if __name__ == "__main__":
    basis_functie()