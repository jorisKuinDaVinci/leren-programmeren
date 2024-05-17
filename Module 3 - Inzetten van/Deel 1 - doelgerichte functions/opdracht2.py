from split_me import *
# Gemiddelde berekenen
def aantal_getallen(getallen):
    return len(getallen)

# Som van alle getallen in de lijst
def som_getallen(getallen):
    return sum(getallen)

# Gemiddelde berekenen
def gemiddelde_getallen(som, aantal):
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

# alle unieke getallen
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