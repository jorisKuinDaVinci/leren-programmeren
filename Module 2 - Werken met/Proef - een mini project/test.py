#ijscoman 1
AARDBEI = CHOCOLADE = VANILLA = 3
#ijs coman 
AARDBEI2 = CHOCOLADE2 = VANILLA2 = 1
#Ijscoman 1
hoeveel_aardbei = int(input(f'Hoeveel aardbei ijs wil je? de prijs is: {AARDBEI} euro ')) 
hoeveel_chocola = int(input(f'Hoeveel chocola ijs wil je? de prijs is: {CHOCOLADE} euro ')) 
hoeveel_vanilla = int(input(f'Hoeveel vanilla ijs wil je? de prijs is: {VANILLA} euro vanilla is 1+1 gratis!')) 
#Aparte berekening van de ijsjes
berekening_totaal_aardbei = AARDBEI + hoeveel_aardbei 
berekening_totaal_chocolade = CHOCOLADE + hoeveel_chocola 
berekening_totaal_vanilla = VANILLA + hoeveel_vanilla 
totaal = berekening_totaal_aardbei + berekening_totaal_vanilla + berekening_totaal_chocolade 
print('-------------------------------------------------------------------------------------------') 
print(f'Je hebt {hoeveel_aardbei} besteld de prijs van de aardbei is: {berekening_totaal_aardbei} aardbei is 1+1 gratis')
print(f'Je hebt {hoeveel_chocola} besteld de prijs van de aardbei is: {berekening_totaal_chocolade}')
print(f'Je hebt {hoeveel_aardbei} besteld de prijs van de aardbei is: {berekening_totaal_vanilla}')
print(f'Het totaal van alle ijsjes komt uit op: {totaal}')
print('----------------------------------------------------------------------------------------------')
if hoeveel_vanilla >=1:     print(f'omdat je {hoeveel_vanilla} hebt besteld betaal je voor het vanilla ijs minder!')     
totaal_1_1 = berekening_totaal_vanilla /2
print(f'Het totaal is nu {totaal_1_1}')     
#Berekening van de ijsjes van de tweede 
hoeveel_aardbei2 = int(input(f'Hoeveel aardbei ijs wil je? de prijs is: {AARDBEI} euro ')) 
hoeveel_chocola2 = int(input(f'Hoeveel aardbei ijs wil je? de prijs is: {CHOCOLADE} euro ')) 
hoeveel_vanilla2 = int(input(f'Hoeveel aardbei ijs wil je? de prijs is: {VANILLA} euro ')) 
berekening_totaal_aardbei2 = AARDBEI2 + hoeveel_aardbei 
berekening_totaal_chocolade2 = CHOCOLADE2 + hoeveel_chocola 
berekening_totaal_vanilla2 = VANILLA2 + hoeveel_chocola 
totaal2 = berekening_totaal_aardbei + berekening_totaal_vanilla + berekening_totaal_chocolade 
print('-------------------------------------------------------------------------------------------')
print(f'Je hebt {hoeveel_aardbei2} besteld de prijs van de aardbei is: {berekening_totaal_aardbei2}')
print(f'Je hebt {hoeveel_chocola2} besteld de prijs van de aardbei is: {berekening_totaal_chocolade2}')
print(f'Je hebt {hoeveel_aardbei2} besteld de prijs van de aardbei is: {berekening_totaal_vanilla2}')
print(f'Het totaal van alle ijsjes komt uit op: {totaal2 - totaal_1_1}')
print('----------------------------------------------------------------------------------------------') 
if hoeveel_aardbei2 >=1:     
    print(f'omdat je {hoeveel_aardbei2} hebt besteld betaal je voor het vanilla ijs minder!')     
    totaal_1_1_2 = berekening_totaal_aardbei2 /2
    print(f'Het totaal is nu {totaal_1_1_2}')    
    print(f'Prijs van ijscoman 1 {totaal_1_1_2} prijs iscoman 2 {totaal_1_1}')