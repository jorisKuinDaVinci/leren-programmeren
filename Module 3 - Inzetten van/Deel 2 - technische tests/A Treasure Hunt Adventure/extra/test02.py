from time import sleep
#Maak met python een programma dat een stoplicht simulleert.

#Dit programma volgt eindeloos de volgende stappen:

#Rood (20 seconden lang)
#Groen (30 seconden lang)
#Oranje (10 seconden lang)
#Na stap 3 gaat het programma weer terug naar stap 1.
while True:
    for i in range(20):
        print("rood")
        sleep(1)
    for i in range(30):
        print("groen")
        sleep(1)
    for i in range(10):
        print("oranje")
        sleep(1)