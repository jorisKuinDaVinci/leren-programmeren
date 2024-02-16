# name of student: Joris
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [50,20,10,5,2,1] #

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

while change > 0 and len(coinValues) > 0: #

  coinValue = coinValues.pop(0) #
  nrCoins = change // coinValue #

  if nrCoins > 0: #
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
    change -= nrCoinsReturned * coinValue # 


if change > 0: #
  print('Change not returned: ', str(change) + ' cents') #
else:
  print('done')
