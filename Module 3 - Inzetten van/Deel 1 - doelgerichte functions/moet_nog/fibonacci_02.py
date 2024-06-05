#
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