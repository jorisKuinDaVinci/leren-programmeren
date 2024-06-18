from collections import Counter
import math, random

# Aantal getallen in de lijst
def aantal_getallen(getallen):
    return len(getallen)

# Som van alle getallen in de lijst
def som_getallen(getallen):
    return sum(getallen)

# Gemiddelde berekenen
def gemiddelde(som, aantal):
    return som / aantal

# Het grootste getal in de lijst
def grootste_getal(getallen):
    return max(getallen)

# Het kleinste getal in de lijst
def kleinste_getal(getallen):
    return min(getallen)

# Het eerste getal in de lijst
def eerste_getal(getallen):
    return getallen[0]

# Het kleinste getal gedeeld door het eerste controle getal
def delen1(kleinste_getal, controlegetal1):
    return kleinste_getal / controlegetal1

# Het grootste getal gedeeld door het tweede controle getal
def delen2(grootste_getal, controlegetal2):
    return grootste_getal / controlegetal2

# Alle unieke getallen
def unieke_getallen(getallen):
    return list(set(getallen))

# Aantal unieke elementen in de lijst
def aantal_unieke_elementen(unieke_getallen):
    return len(unieke_getallen)

# Verschil tussen aantal unieke elementen en eerste controle getal
def verschil1(aantal_unieke_elementen, controlegetal1):
    return abs(aantal_unieke_elementen - controlegetal1)

# Sorteer de lijst van getallen
def gesorteerde_lijst(getallen):
    return sorted(getallen)

# Sorteer de lijst van unieke getallen
def gesorteerde_lijst_uniek(unieke_getallen):
    return sorted(unieke_getallen)

# Tel het aantal keren dat elk uniek element voorkomt in de lijst
def telling_elementen(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal] + 1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

# Getallen die deelbaar zijn door het eerste controle getal
def deelbaar1(unieke_getallen, controlegetal1):
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    return sorted(deelbaar1)

# Getallen die deelbaar zijn door het tweede controle getal
def deelbaar2(unieke_getallen, controlegetal2):
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    return sorted(deelbaar2)

# Controleer of een bepaald getal in de lijst voorkomt
def komtvoor(getallen, controlegetal1, controlegetal2):
    return controlegetal1 in getallen and controlegetal2 in getallen

# Vindt de posities van het eerste controle getal
def posities(getallen, controlegetal1):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

# Standaardafwijking berekenen
def standaardafwijking(getallen):
    gem = sum(getallen) / len(getallen)
    verschil_kwadraat = sum((x - gem) ** 2 for x in getallen)
    variantie = verschil_kwadraat / len(getallen)
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

# Shuffle de lijst
def shuffle_lijst(getallen):
    random.shuffle(getallen)
    return getallen

# Pak een random getal uit de lijst
def random_getal(getallen):
    return getallen[random.randint(0, len(getallen) - 1)]

# Verschil tussen twee getallen
def verschil2(random_getal, controlegetal2):
    return abs(random_getal - controlegetal2)

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

    resultaten = {
        "Aantal getallen": aantal_getallen,
        "Gemiddelde": gemiddelde,
        "Som": som_getallen,
        "Grootste getal": grootste_getal,
        "Kleinste getal": kleinste_getal,
        "Eerste getal": eerste_getal,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": getallen,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")