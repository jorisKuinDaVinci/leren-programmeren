import time
from termcolor import colored
import math
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY

##################### O03 #####################

def copper2silver(amount:int) -> float:
    # 10 koper = 1 zilver
    return amount / 10

def silver2gold(amount:int) -> float:
    # 5 zilver = 1 goud
    return amount / 5

def copper2gold(amount:int) -> float:
    # 10 koper = 1 zilver
    # 5 zilver = 1 goud
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    # 25 goud = 1 platina
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    return platinum2gold(personCash['platinum']) + copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + personCash['gold']

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    # 4 koper per dag per persoon
    # 3 koper per dag per paard
    # 11 dagen
    return (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS / 50

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item.get(key) == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    if not getFromListByKeyIs(friends, 'shareWith', True):
        return []
    return getFromListByKeyIs(friends, 'adventuring', True)

##################### O07 #####################
#Geen tenten en 1 paard, ja dat is inderdaad niet heel handig als je op een avontuur van 11 dagen gaat. 
#Na wat navragen in het dorp hebben ze op de volgende informatie vergaard: 
#In de tenten (die ze kunnen huren) kunnen max 3 personen slapen en op ieder paard kunnen 2 personen rijden. 
#Een paard huren kost 5 zilver per dag en een tent huren kost 3 goud per week ongeacht hoeveel dagen je hem die week gebruikt.
#Zorg weer voor een errorloze applicatie na het invullen van de volgende 3 functies: 
#getNumberOfHorsesNeeded, getNumberOfTentsNeeded en getTotalRentalCost.
#Voor deze functies heb je de library math nodig met de functie ceil.

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    #met de hulp van de 003 functions, de nieuwe constanten en JOURNEY_IN_DAYS.
    # totaal in float omdat er goud en zilver in zit.
    return (horses * COST_HORSE_SILVER_PER_DAY + tents * COST_TENT_GOLD_PER_WEEK) * JOURNEY_IN_DAYS / 5 # 5 zilver = 1 goud
    #return (horses * COST_HORSE_SILVER_PER_DAY + tents * COST_TENT_GOLD_PER_WEEK) * JOURNEY_IN_DAYS / 5 # 5 zilver = 1 goud

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()