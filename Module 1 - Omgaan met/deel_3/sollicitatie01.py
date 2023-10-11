# Opdracht: Sollicitatiebrief schrijven
practice_dieren_dressuur = int(input("hoeveel praktijkervaring heb je met dieren-dressuur? "))
experience = int(input("hoeveel jaar praktijkervaring heb je met jongleren? "))
practice_acrobatiek = int(input("hoeveel jaar praktijkervaring heb je met acrobatiek? "))
certificaat = input("ben je in bezit van certificaat overleven met gevaarlijk personeel? ")
vrachtwagen_rijbewijs = input("ben je in bezit van een geldig vrachtwagen rijbewijs? ")
hoge_hoed = input("ben je in bezit van een hoge hoed? ")
lichaamsgewicht = int(input("wat is je lichaamsgewicht? "))
lengte = int(input("hoe lang ben je? "))
MIN_WEIGHT = 90
MAX_WEIGHT = 120
MIN_LENGTH = 150
MAX_LENGTH = 220
MIN_PRACTICE_DIEREN_DRESSUUR = 4
MIN_EXPERIENCE = 5
MIN_PRACTICE_ACROBATIEK = 3
if (practice_dieren_dressuur >= MIN_PRACTICE_DIEREN_DRESSUUR or experience >= MIN_EXPERIENCE or practice_acrobatiek >= MIN_PRACTICE_ACROBATIEK) and certificaat == "ja" and vrachtwagen_rijbewijs == "ja" and hoge_hoed == "ja" and lichaamsgewicht >= MIN_WEIGHT and lichaamsgewicht <= MAX_WEIGHT and lengte >= MIN_LENGTH and lengte <= MAX_LENGTH:
    print("gefeliciteerd, je bent aangenomen!")
else: 
    print("sorry, je bent niet aangenomen")