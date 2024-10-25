import time
from termcolor import colored
import math
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY, COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT

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
#Na het zien van de prijs is de eerste reactie: “oei, dat is wel erg veel. 
# Zoveel hebben we niet!”, maar je kan het ook zien als een uitdaging. 
# Misschien moeten we als groep naar investeerders op zoek. 
# Ze moeten alleen niet meer dan 10% (van de opbrengst) vragen want daar hebben we geen interresse in. Sommige investeerders zullen wel mee gaan en andere niet, dus er moet wel uitgerekend worden wat de kosten voor de investeerders is. 
# Een investeerder die mee gaat wil een eigen tent, een eigen paard, een eigen uitrusting en natuurlijk het eten voor de reis.
#Maak het zo dat de juiste investeerders geselecteerd worden en dat de extra kosten berekend worden.

def getInterestingInvestors(investors: list) -> list:
    # getInterestingInvestors om te weten wat interresante investeerders zijn moet je de tekst bovenaan lezen.
    interestinginvestors = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            interestinginvestors.append(investor)
    return interestinginvestors
    #return [investor for investor in investors if investor['profitReturn'] <= 10]

def getAdventuringInvestors(investors: list) -> list:
    #getAdventuringInvestors dit zijn de investeerders, die interessant zijn en de property  ‘adventuring’ op True hebben staan.
    return [investor for investor in getInterestingInvestors(investors) if investor['adventuring']]

def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    #getTotalInvestorsCosts rekent uit wat alle investeerders die mee gaan, kosten.
    total_cost = 0.0
    for investor in getAdventuringInvestors(investors):
        total_cost += getItemsValueInGold(gear) + getJourneyFoodCostsInGold(1, 1) + getTotalRentalCost(1, 1)
    return total_cost

##################### O11 #####################
#Wat is die Dwindel toch een watje, hij kan niet eens alle nachten in een tent overnachten, maar hij is 1 van de twee waar het geld vandaan komt. 
# Dus laten we hem maar helpen om zoveel mogelijk in een herberg te overnachten.
#Reken uit hoeveel nachten er maximaal overnacht kan worden met het goud dat overgebleven is na alle inkopen.

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    # Bereken de kosten per nacht voor personen en paarden
    cost_per_night = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses + silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    # Bereken hoeveel nachten de groep in een herberg kan blijven
    return math.floor(leftoverGold / cost_per_night)

def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    # Bereken de kosten per nacht voor de mensen (in goud omgerekend van zilver)
    cost_per_night_people_in_gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    
    # Bereken de kosten per nacht voor de paarden (in goud omgerekend van koper)
    cost_per_night_horses_in_gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    
    # Totale kosten per nacht voor zowel mensen als paarden
    total_cost_per_night_in_gold = cost_per_night_people_in_gold + cost_per_night_horses_in_gold
    
    # Totale kosten voor het aantal nachten
    total_journey_inn_costs_in_gold = total_cost_per_night_in_gold * nightsInInn
    
    return round(total_journey_inn_costs_in_gold, 2)  # Afronden naar 2 decimalen

##################### O13 #####################
#Met zo'n 900 goud te verdelen begonnen ze te rekenen. 
# Allereerst krijgen de investeerders hun “profit return” van de 900 goud en met wat overbijft moet nog uitgerekend worden wat iedereen die op avontuur is meegegaan krijgt. 
# (Let op: er kunnen vrienden maar ook investeerders meegaan!)
#Bereken wat de interesante investeerders krijgen en wat iedere avonturier krijgt.

def getInvestorsCuts(profitGold: float, investors: list) -> list:
    # Alleen investeerders met een profitReturn <= 10 krijgen een aandeel
    interesting_investors = getInterestingInvestors(investors)
    investors_cuts = []
    
    for investor in interesting_investors:
        # Bereken de winst voor de investeerder op basis van hun profitReturn percentage
        cut = (profitGold * investor['profitReturn']) / 100
        investors_cuts.append(round(cut, 2))  # Rond af op 2 decimalen voor nauwkeurigheid
    
    return investors_cuts

def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    # Trek de totale winst die naar investeerders gaat af van het totale winstbedrag
    total_investors_cut = sum(investorsCuts)
    remaining_gold = max(profitGold - total_investors_cut, 0)  # Zorgt dat remaining_gold niet negatief is

    # Verdeel het resterende goud over de avonturiers (fellowship)
    if fellowship > 0:
        adventurer_cut = remaining_gold / fellowship
    else:
        adventurer_cut = 0.0  # Geen verdeling als er geen avonturiers zijn

    return round(adventurer_cut, 2)  # Rond af op 2 decimalen voor nauwkeurigheid

##################### O14 #####################
#Het enige dat nog te doen is, is om de balans op te maken. 
# De vrienden (die mee gaan) van de avonturier zijn zo blij met de kans om geld te verdienen, dat ieder van hen besluit om de avonturier 10 goud van hun winst te geven.
#Bereken voor iedere persoon (ook de mensen die niet mee hebben gedaan), met hoeveel goud ze starten en met hoeveel goud ze het verhaal eindigen.
#getEarnigs geeft een lijst met dictonairies terug, een dictionairy heeft 3 properties en ziet er zo uit:
# {
#     'name': 'Rudi',
#     'start': 3.5,
#     'end': 243.9
# }
def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = []
    interestingInvestors = []
    adventuringInvestors = []
    investorsCuts = []
    goldCut = 0.0

    # verdeel de uitkomsten
    for person in people:
        #code aanvullen

        earnings.append({
            'name'   : '??',
            'start'  : 0.0,
            'end'    : 0.0
        })

    return earnings

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