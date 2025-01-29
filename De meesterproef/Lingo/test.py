from functions import controleer_letters
from termcolor import colored

def test_controleer_letters():
    """Test de functie controleer_letters met verschillende invoer."""
    te_raden_woord = "appel"
    
    # Test 1: Exact goed
    gok = "appel"
    expected = " ".join([colored(c, "green") for c in gok])
    result = controleer_letters(gok, te_raden_woord)
    assert result == expected, f"Test 1 mislukt! Verwacht: {expected}, gekregen: {result}"
    print("Test 1 geslaagd: Exact goed")
    
    # Test 2: Een paar letters goed, een paar verkeerd
    gok = "aplus"
    expected = f"{colored('a', 'green')} {colored('p', 'green')} {colored('l', 'yellow')} {colored('u', 'red')} {colored('s', 'red')}"
    result = controleer_letters(gok, te_raden_woord)
    assert result == expected, f"Test 2 mislukt! Verwacht: {expected}, gekregen: {result}"
    print("Test 2 geslaagd: Gedeeltelijk goed")
    
    # Test 3: Helemaal fout
    gok = "zoets"
    expected = " ".join([colored(c, "red") for c in gok])
    result = controleer_letters(gok, te_raden_woord)
    assert result == expected, f"Test 3 mislukt! Verwacht: {expected}, gekregen: {result}"
    print("Test 3 geslaagd: Helemaal fout")
    
    # Test 4: Letters op verkeerde plek
    gok = "lapep"
    expected = f"{colored('l', 'yellow')} {colored('a', 'green')} {colored('p', 'green')} {colored('e', 'green')} {colored('p', 'yellow')}"
    result = controleer_letters(gok, te_raden_woord)
    assert result == expected, f"Test 4 mislukt! Verwacht: {expected}, gekregen: {result}"
    print("Test 4 geslaagd: Letters op verkeerde plek")
    
if __name__ == "__main__":
    test_controleer_letters()
    print("Alle tests zijn succesvol uitgevoerd!")