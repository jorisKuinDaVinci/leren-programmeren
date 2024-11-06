def cijfers(reeks):
    resultaat = ""
    i = 0
    while i < len(reeks):
        tel = 1
        while i + 1 < len(reeks) and reeks[i] == reeks[i + 1]:
            i += 1
            tel += 1
        resultaat += str(tel) + reeks[i]
        i += 1
    return resultaat

def genereer_reeks():
    reeks = "1"
    stap = 1
    while "33" not in reeks:
        print(f"Stap {stap}: {reeks}")
        reeks = cijfers(reeks)
        stap += 1
    print(f"Stap {stap}: {reeks} (bevat '2 x 3')")

genereer_reeks()