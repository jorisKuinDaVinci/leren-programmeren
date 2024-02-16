coinValues = [50,20,10,5,2,1] # de waardes van de munten

toPay = int(float(input('Amount to pay: '))* 100) # input van wat je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # input van wat je hebt betaald 
change = paid - toPay # wat je hebt betaald - wat je moet betalen

while change > 0 and len(coinValues) > 0: # zolang er nog wisselgeld is en er nog munten zijn

  coinValue = coinValues.pop(0) # coinValue is de eerste waarde van coinValues
  nrCoins = change // coinValue # wat je terug krijgt / de waarde van de munt

  if nrCoins > 0: # als je munten terug krijgt
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # hoeveel munten je terug krijgt
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # hoeveel munten je teruggeeft
    change -= nrCoinsReturned * coinValue # wat je terug krijgt - wat je hebt teruggegeven * de waarde van de munt


if change > 0: # als je nog steeds wisselgeld hebt
  print('Change not returned: ', str(change) + ' cents') # wat je terug krijgt
else:
  print('done')
