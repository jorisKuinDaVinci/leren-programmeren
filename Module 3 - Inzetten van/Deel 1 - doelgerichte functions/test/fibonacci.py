#De fibonacci reeks is een bekende getallenreeks die zijn oorsprong vind in het jaar 1202. Beschreven door Leonardo van Pisa.
#Deze reeks heeft verschillende interessante eigenschappen en wordt vaak in relatie gelegd met de "gulden snede".
#De fibonacci reeks is een reeks van getallen waarbij elk van deze getallen een bepaald verband heeft met de voorgaande getallen. 
#Hier een voorbeeld van de eerste tien getallen (gescheiden door komma's) uit de reeks:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34 
#Elk volgend getal in de reeks bereken je als de som van de twee voorgaande getallen.
#Alleen de eerste 2 getallen uit de reeks zijn niet te berekenen: 0 en 1. 
#De gulden snede bereken je als de deling van een getal uit de reeks door het eerstvolgende getal uit de reeks.

#in deze opdracht ga je een programma maken die een aantal getallen uit de getallenreeks berekent en op het scherm toont.
#Het programma moet de gulden snede teruggeven die is berekend op basis van de laatste 2 berekende getallen uit de geprinte reeks.
#Je maakt in de uitwerking ten minste gebruik van de volgende onderdelen:

#Variabelen
#Loops
#Functions
#Parameters (en dus ook arguments)
#Returnwaarden
 

#Denk aan de volgende regels voor goede functions:

#Gebruik geen global variabelen: wissel gegevens met functions alleen uit via parameters en returns
#Laat een function maar één taak uitvoeren.
#Geef een function een naam die precies aanduidt wat de taak is.

def fibonacci(reeks):
    getallen = [0, 1]
    for i in range(2, reeks):
        getallen.append(getallen[i-1] + getallen[i-2])
    print(getallen)
    return getallen[-1] / getallen[-2]
    
reeks = int(input('Hoeveel getallen wil je in de reeks?(Het getal moet groter zijn dan 2.) '))

print(f'Gulden snede: {fibonacci(reeks)}')