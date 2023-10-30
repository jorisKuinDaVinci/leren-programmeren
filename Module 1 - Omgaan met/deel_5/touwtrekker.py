#Maak de Python applicatie "Touw Trekker" in touwtrekker.py. Deze app wordt gebruikt in de bouwmarkt.

#De functionaliteiten die in de applicatie moeten zitten:

#de klant kan een keuze maken uit 3 diktes touw, namelijk: 3, 4.5 en 6.3. Voor elke dikte wordt er gevraagd hoeveel stukken de klant wilt.
#Voor elke dikte wordt ook gevraagd wat de lengte van de stukken (in meters) moeten zijn. Je mag een willekeurig getal opgeven, ook een getal met decimalen. Bijvoorbeeld 4.3
#Prijzen per meter voor elke dikte mag je zelf verzinnen. Bijvoorbeeld: 1.23, 2.45 en 4.10
#Toon op het scherm per dikte:
#de dikte
#het aantal stukken
#hun lengte
#de totaalprijs
#Toon op het scherm de totaalprijs van alle touw.
#Bovenaan in de Python file noteer je als commentaar het volgende: voornaam, achternaam en opdracht: Touw trekker
#De volgende zaken dienen ook op orde te zijn:

#leesbare layout van de code
#naamgeving is duidelijk en 'self explaining'
#er is passend commentaar toegevoegd in de code
#laat de uitkomst er uit zien als een bonnetje

#Voorbeeld van de uitkomst:
#Touw Trekker
#Dikte: 3.0
#Aantal stukken: 2
#Lengte: 4.3
#Totaalprijs: 10.34
dikte_3 = 3.0
dikte_4_5 = 4.5
dikte_6_3 = 6.3
prijs_3 = 1.23
prijs_4_5 = 2.45
prijs_6_3 = 4.10
print("Touw Trekker")
print("--------------------------------------------------------")
print("Dikte: " + str(dikte_3))
aantal_stukken_3 = int(input("Hoeveel stukken wil je? "))
lengte_3 = float(input("Hoe lang moeten de stukken zijn? "))
totaalprijs_3 = prijs_3 * lengte_3 * aantal_stukken_3
print("Totaalprijs: " + str(totaalprijs_3))
print("--------------------------------------------------------")
print("Dikte: " + str(dikte_4_5))
aantal_stukken_4_5 = int(input("Hoeveel stukken wil je? "))
lengte_4_5 = float(input("Hoe lang moeten de stukken zijn? "))
totaalprijs_4_5 = prijs_4_5 * lengte_4_5 * aantal_stukken_4_5
print("Totaalprijs: " + str(totaalprijs_4_5))
print("--------------------------------------------------------")
print("Dikte: " + str(dikte_6_3))
aantal_stukken_6_3 = int(input("Hoeveel stukken wil je? "))
lengte_6_3 = float(input("Hoe lang moeten de stukken zijn? "))
totaalprijs_6_3 = prijs_6_3 * lengte_6_3 * aantal_stukken_6_3
print("Totaalprijs: " + str(totaalprijs_6_3))
print("--------------------------------------------------------")
totaalprijs = totaalprijs_3 + totaalprijs_4_5 + totaalprijs_6_3
print("Totaalprijs: " + str(totaalprijs))
print("--------------------------------------------------------")
print("Bedankt voor uw aankoop!")