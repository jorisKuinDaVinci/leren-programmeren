# To do:
# volgorde:
# eerst de inports
# dan de functies
# dan de variabele
# dan de programma code

PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

bandje = False
stempel = False

complimenten_van_het_huis = "alsjeblieft, complimenten van het huis"
geen_alcohol = "Sorry, je mag geen alcohol bestellen onder de 21"
alleen_vip_champagne = "Sorry, alleen VIP's mogen champagne bestellen"
geen_idee_krijg_water = "Sorry, geen idee wat je bedoelt, hier een glaasje water"
niet_naar_binnen = "Sorry, je mag niet naar binnen"
stempel_tekst = "je krijgt van mij een stempel"

def tot_je_18_bent(Hoe_oud):
    tot_je_18_bent_som = 18 - int(Hoe_oud)
    print(f"Probeer het in " + str(tot_je_18_bent_som) + " jaar nog eens")    
    return

def wat_wil_je_drinken(bandje):
    print("Wat wil je drinken?")
    drankje = input("Maak je keuze: ").lower
    if drankje not in DRANKJES:
        print(geen_idee_krijg_water)
        drankje = "water"
        return
    else:
        if drankje == "cola":
            if bandje == True:
                print(complimenten_van_het_huis)
                return
            else:
                print(f"je {drankje} is dan " + str(PRIJS_COLA))
                return
        elif drankje == "bier":
            if bandje == True or stempel == True:
                if bandje == True:
                    print(complimenten_van_het_huis)
                    return
                else:
                    print(f"je {drankje} is dan " + str(PRIJS_BIER))
                    return
            else:
                print(geen_alcohol)
                tot_je_18_bent()
        elif drankje == "champagne":
            if bandje == True:
                if bandje_klaur == "blauw":
                    print(f"je {drankje} is dan " + str(PRIJS_CHAMPAGNE))
                    return
                else:
                    print(geen_alcohol)
                    tot_je_18_bent()
            else:
                print(alleen_vip_champagne)
                return
    return drankje

Hoe_oud = input("Hoe oud ben je?")
if int(Hoe_oud) >= 18:
    naam = input("Wat is je naam?")
    if naam in VIP_LIST:
        VIP = True
        if Hoe_oud >= 21:
            bandje_klaur = "blauw"
            bandje = True
        else:
            bandje_klaur = "rood"
            bandje = True
        print("Je krijgt een " + bandje_klaur + " bandje")   
    else:
        VIP = False
        if int(Hoe_oud) >= 21:
            print(stempel_tekst)
            stempel = True   
    wat_wil_je_drinken()  
else:
    print(niet_naar_binnen) 
    tot_je_18_bent()     