# Deel 2 - collections - Deck van speelkaarten
import random

kleuren = ("harten", "klaveren", "schoppen", "ruiten")

kaarten = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")

jokers = ("joker", "joker")

deck = []

for i in range(len(kleuren)):
    for j in range(len(kaarten)):
        deck.append(kaarten[j] + " " + kleuren[i])
        # haal de kaart uit het deck

for i in range(len(jokers)):
    deck.append(jokers[i])

random.shuffle(deck)

# 7 kaarten

for i in range(7):
    print("Kaart " + str(i + 1) + ": " + deck[i])

#for i in range(len(deck)):
    #print("Kaart " + str(i + 1) + ": " + deck[i])

print("deck (" + str(len(deck)) + "kaarten): " + str(deck))
