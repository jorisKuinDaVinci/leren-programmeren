import time
from termcolor import colored
from data import JOURNEY_IN_DAYS

##################### O03 #####################

def copper2silver(amount:int) -> float:
    copper = amount
    silver = copper // 100
    copper = copper % 100
    return silver + copper / 100

def silver2gold(amount:int) -> float:
    silver = amount
    gold = silver // 100
    silver = silver % 100
    return gold + silver / 100

def copper2gold(amount:int) -> float:
    copper = amount
    gold = copper // 10000
    copper = copper % 10000
    silver = copper // 100
    copper = copper % 100
    return gold + silver / 100 + copper / 10000

def platinum2gold(amount:int) -> float:
    platinum = amount
    gold = platinum * 10
    return gold

def getPersonCashInGold(personCash:dict) -> float:
    copper = personCash['copper']
    silver = personCash['silver']
    gold = personCash['gold']
    platinum = personCash['platinum']
    return copper2gold(copper) + silver2gold(silver) + gold + platinum2gold(platinum)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    pass

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    pass

def getAdventuringPeople(people:list) -> list:
    people = getFromListByKeyIs(people, 'adventuring', True)
    return people

def getShareWithFriends(friends:list) -> list:
    friends = getFromListByKeyIs(friends, 'share', True)

def getAdventuringFriends(friends:list) -> list:
    friends = getFromListByKeyIs(friends, 'adventuring', True)

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    peoplePerHorse = 2
    horses = people // peoplePerHorse
    if people % peoplePerHorse > 0:
        horses += 1
    return horses

def getNumberOfTentsNeeded(people:int) -> int:
    peoplePerTent = 4
    tents = people // peoplePerTent
    if people % peoplePerTent > 0:
        tents += 1
    return tents

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    itemsValue = 0
    for item in items:
        itemsValue += item['value']
    return itemsValue

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    cash = 0
    for person in people:
        cash += getPersonCashInGold(person['cash'])
    return cash

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