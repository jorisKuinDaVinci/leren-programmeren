# Opdracht: Sollicitatiebrief schrijven
practice_dieren_dressuur = int(input("hoeveel praktijkervaring heb je met dieren-dressuur? "))
experience = int(input("hoeveel jaar praktijkervaring heb je met jongleren? "))
practice_acrobatiek = int(input("hoeveel jaar praktijkervaring heb je met acrobatiek? "))
certificaat = input("ben je in bezit van certificaat overleven met gevaarlijk personeel? ")
diploma = input("ben je in bezit van een MBO-4 diploma? ")
ondernemer = input("ben je ondernemer? ")
if ondernemer == "ja":
    ondernemer_years = int(input("hoeveel jaar ben je ondernemer? "))
    werknemers = int(input("hoeveel werknemers heb je in dienst? "))
else:
    ondernemer_years = 0
    werknemers = 0
geslacht = input("wat is je geslacht? ")
if geslacht == "man":
    snor = input("heb je een snor? ")  
    if snor == "ja":
        snor_length = int(input("hoe lang is je snor? "))
    else:
        snor = "nee"
        snor_length = 0
if geslacht == "vrouw":
   krulhaar = input("heb je rood krulhaar? ")
   if krulhaar == "ja":
       krulhaar_length = int(input("hoe lang is je rode krulhaar? "))
   else:
       krulhaar = "nee"
       krulhaar_length = 0
if geslacht == "anders":
    Brede_glimlach = input("heb je een brede glimlach? ")
    if Brede_glimlach == "ja":
        Brede_glimlach_breedte = int(input("hoeveel cm is je brede glimlach? "))
    else:
        Brede_glimlach = "nee"
        Brede_glimlach_breedte = 0                  
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
MIN_ONDERNEMER_YEARS = 3
MIN_WERKNEMERS = 5
MIN_SNOR_LENGTH = 10
MIN_ROOD_KRULHAAR_LENGTH = 20
MIN_BREDE_GLIMLACH_BREEDTE = 10
if (practice_dieren_dressuur >= MIN_PRACTICE_DIEREN_DRESSUUR or experience >= MIN_EXPERIENCE or practice_acrobatiek >= MIN_PRACTICE_ACROBATIEK) and certificaat == "ja" and vrachtwagen_rijbewijs == "ja" and hoge_hoed == "ja" and lichaamsgewicht >= MIN_WEIGHT and lichaamsgewicht <= MAX_WEIGHT and lengte >= MIN_LENGTH and lengte <= MAX_LENGTH and (diploma == "ja" or ondernemer == "ja" and ondernemer_years > MIN_ONDERNEMER_YEARS and werknemers >= MIN_WERKNEMERS) and geslacht == "man" and snor == "ja" and snor_length > MIN_SNOR_LENGTH or geslacht == "vrouw" and krulhaar == "ja" and krulhaar_length > MIN_ROOD_KRULHAAR_LENGTH or geslacht == "anders" and Brede_glimlach == "ja" and Brede_glimlach_breedte > MIN_BREDE_GLIMLACH_BREEDTE:
    print("gefeliciteerd, je bent aangenomen!")
else:
    print("sorry, je bent niet aangenomen")