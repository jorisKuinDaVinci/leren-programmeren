def genereer_fibonacci_reeks(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_reeks = [0, 1]
    for i in range(2, n):
        volgende_nummer = fib_reeks[-1] + fib_reeks[-2]
        fib_reeks.append(volgende_nummer)
    return fib_reeks

def genereer_gulden_snede(a, b):
    if b == 0:
        return None
    return a / b

# Aantal getallen in de Fibonacci reeks
aantal_getallen_fibonacci_reeks = 10

# Genereer de Fibonacci reeks
fibonacci_reeks = genereer_fibonacci_reeks(aantal_getallen_fibonacci_reeks)

    # Bereken de Gulden Snede op basis van de laatste twee getallen
if len(fibonacci_reeks) < 2:
    print("Niet genoeg getallen in de reeks om de Gulden Snede te berekenen.")
    exit()

laatste_nummer = fibonacci_reeks[-1]
tweede_laatste_nummer = fibonacci_reeks[-2]
gulden_snede = genereer_gulden_snede(laatste_nummer, tweede_laatste_nummer)

# Print de resultaten
print(f"Eerste {aantal_getallen_fibonacci_reeks} getallen van de Fibonacci-reeks: {', '.join(map(str, fibonacci_reeks))}")
print(f"De Gulden Snede berekend op basis van de laatste twee getallen ({laatste_nummer} en {tweede_laatste_nummer}) is: {gulden_snede}")