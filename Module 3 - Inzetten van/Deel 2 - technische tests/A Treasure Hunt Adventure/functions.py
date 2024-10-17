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

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    # Bereken kosten voor paarden in goud
    #horse_cost_in_silver = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    #horse_cost_in_gold = silver2gold(horse_cost_in_silver)
    horse_cost_in_gold = silver2gold(horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS)
    
    # Bereken kosten voor tenten in goud (2 weken nodig voor 11 dagen)
    tent_cost_in_gold = tents * COST_TENT_GOLD_PER_WEEK * 2  # 11 dagen betekent 2 weken huur

    # Totaal kosten in goud
    total_cost_in_gold = horse_cost_in_gold + tent_cost_in_gold
    return total_cost_in_gold

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    # Format elke item in de lijst
    formatted_items = [
        f"{item['amount']}{item['unit']} {item['name']}" for item in items
    ]
    # Voeg items samen met komma's en "&" voor de laatste item
    if len(formatted_items) > 1:
        return ', '.join(formatted_items[:-1]) + ' & ' + formatted_items[-1]
    elif formatted_items:
        return formatted_items[0]
    else:
        return ""

def getItemsValueInGold(items: list) -> float:
    total_value_in_gold = 0.0
    
    for item in items:
        amount = item['price']['amount']
        price_type = item['price']['type']
        
        # Zet elke prijs om naar goud
        if price_type == 'copper':
            total_value_in_gold += copper2gold(amount) * item['amount']
        elif price_type == 'silver':
            total_value_in_gold += silver2gold(amount) * item['amount']
        elif price_type == 'gold':
            total_value_in_gold += amount * item['amount']
        elif price_type == 'platinum':
            total_value_in_gold += platinum2gold(amount) * item['amount']
    
    return total_value_in_gold

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    cash_in_gold = 0.0
    for person in people:
        cash_in_gold += getPersonCashInGold(person['cash'])
    return cash_in_gold

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    return getFromListByKeyIs(investors, 'profitReturn', 5)

def getAdventuringInvestors(investors:list) -> list:
    return getFromListByKeyIs(investors, 'adventuring', True)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total_cost = 0.0
    for investor in investors:
        if investor['adventuring']:
            total_cost += getItemsValueInGold(gear) * investor['profitReturn'] / 100
        else:
            total_cost += getItemsValueInGold(gear) * investor['profitReturn'] / 100 * 2
    return total_cost

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