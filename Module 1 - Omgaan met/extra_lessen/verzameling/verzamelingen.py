#tekst = "Dit is een tekst" # eenvoudig voorbeeld van een verzameling van karakters
#tekst_2 = "a" # eenvoudig voorbeeld van een verzameling van karakters

#for x in range(len(tekst)): # dit is de manier om net zo vaak code uit te voeren als dat je vooraf wilt weten.
    #print(tekst[x])

#print("2e keer")
#for c in tekst: # de c verandert per iteratie in het karater wat dan aan de beurt is. Hij begint bij index 0
    #print("De letter die nu aan de beurt is: {c}")
    #print(c)    

tekst_3 = "Abba was erg populair in de jaren 70"
# schrijf code die het aantal a's uitrekent in deze string!
aantal_a = 0
for c in tekst_3:
    if c == "a" or c == "A":
        print(c)
        aantal_a = aantal_a + 1
print(aantal_a)
