def genereer_fibonacci_reeks(aantal_getallen_fibonacci_reeks):
    if aantal_getallen_fibonacci_reeks <= 0:
        return []
    elif aantal_getallen_fibonacci_reeks == 1:
        return [0]
    elif aantal_getallen_fibonacci_reeks == 2:
        return [0, 1]
    
    fib_reeks = [0, 1]
    for _ in range(2, aantal_getallen_fibonacci_reeks):
        volgende_nummer = fib_reeks[-1] + fib_reeks[-2]
        fib_reeks.append(volgende_nummer)
    return fib_reeks

def genereer_gulden_snede(laatste_nummer, tweede_laatste_nummer):
    if tweede_laatste_nummer == 0:
        return None
    return laatste_nummer / tweede_laatste_nummer

# Aantal getallen in de Fibonacci reeks
aantal_getallen_fibonacci_reeks = 10

# Genereer de Fibonacci reeks
fibonacci_reeks = genereer_fibonacci_reeks(aantal_getallen_fibonacci_reeks)

# Bereken de Gulden Snede op basis van de laatste twee getallen
if len(fibonacci_reeks) < 2:
    print("Niet genoeg getallen in de reeks om de Gulden Snede te berekenen.")
else:
    laatste_nummer = fibonacci_reeks[-1]
    tweede_laatste_nummer = fibonacci_reeks[-2]
    gulden_snede = genereer_gulden_snede(laatste_nummer, tweede_laatste_nummer)

    # Print de resultaten
    print(f"Eerste {aantal_getallen_fibonacci_reeks} getallen van de Fibonacci-reeks: ")
    for i in range(len(fibonacci_reeks)):
        if i == len(fibonacci_reeks) - 1:
            print(fibonacci_reeks[i])
        else:
            print(fibonacci_reeks[i], ", ")
    print(f"De Gulden Snede berekend op basis van de laatste twee getallen ({laatste_nummer} en {tweede_laatste_nummer}) is: {gulden_snede}")