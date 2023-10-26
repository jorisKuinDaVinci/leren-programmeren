from studieadviestext import *
print(STUDIEDOKTER_TITEL)
hoeveel_weken = int(input(AANTAL_WEKEN_VRAAG))
stress_blokkades = int(input(COMPETENTIE_STELLING_1 + OPTIES))
uitstellen = int(input(COMPETENTIE_STELLING_2 + OPTIES))
talent = int(input(COMPETENTIE_STELLING_3 + OPTIES))
vermijd_assessments = int(input(COMPETENTIE_STELLING_4 + OPTIES)) 
vergelijk = int(input(COMPETENTIE_STELLING_5 + OPTIES))
if hoeveel_weken >= 10:
    interesse = int(input(COMPETENTIE_STELLING_6 + OPTIES))
    kopieer = int(input(COMPETENTIE_STELLING_7 + OPTIES))

#gemiddelde_score = stress_blokkades + uitstellen + talent + vermijd_assessments + vergelijk
if hoeveel_weken >= 10:
    gemiddelde_score = stress_blokkades + uitstellen + talent + vermijd_assessments + vergelijk + interesse + kopieer
else:
    gemiddelde_score = stress_blokkades + uitstellen + talent + vermijd_assessments + vergelijk
#gemiddelde_score = (stress_blokkades + uitstellen + talent + vermijd_assessments + vergelijk) / 5
print(str(gemiddelde_score))
print(COMPETENTIE_ADVIES_TITEL)
if gemiddelde_score <= 2 or (stress_blokkades <= 1 or uitstellen <= 1 or talent <= 1 or vermijd_assessments <= 1 or vergelijk <= 1 or interesse <= 1 or kopieer <= 1):
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde_score <= 3 or (stress_blokkades <= 2 or uitstellen <= 2 or talent <= 2 or vermijd_assessments <= 2 or vergelijk <= 2 or interesse <= 2 or kopieer <= 2):
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)    