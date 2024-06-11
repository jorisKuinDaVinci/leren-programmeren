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