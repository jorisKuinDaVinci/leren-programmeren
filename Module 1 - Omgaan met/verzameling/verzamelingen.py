tekst = "Dit is een tekst" # eenvoudig voorbeeld van een verzameling van karakters
tekst_2 = "a" # eenvoudig voorbeeld van een verzameling van karakters

for x in range(len(tekst)): # dit is de manier om net zo vaak code uit te voeren als dat je vooraf wilt weten.
    print(tekst[x])

print("2e keer")
for c in tekst: # de c verandert per iteratie in het karater wat dan aan de beurt is. Hij begint bij index 0
    print("De letter die nu aan de beurt is: {c}")
    print(c)    