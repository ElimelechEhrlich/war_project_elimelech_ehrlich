import random

def create_card(rank:str,suite:str):
    ranks = {'2' : '2' , '3' : '3' , '4' : '4' , '5' : '5' , '6' : '6' , '7' : '7' , '8' : '8' , '9' : '9' , '10' : '10' ,  'J' : '11' , 'Q' : '12' , 'K' : '13' , 'A' : '14'}
    suites = ['H', 'C', 'D', 'S']
    if rank in ranks.keys() and suite in suites:
        return ({'rank': rank, 'suite': suite, 'value': ranks[rank]})
    else:
        return ('Incorrect suite or rank input')
    

def compare_cards(p1_card:dict, p2_card:dict):
    try:
        if p1_card['rank'] > p2_card['rank']:
            return ('p1')
        elif p2_card['rank'] > p1_card['rank']:
            return ('p2')
        elif p2_card['rank'] == p1_card['rank']:
            return ('WAR')
    except:
        print (f'"value" key is does not exist in Or its value is not of type number at least one of the dictionaries')
    return
                                      
def create_deck(): 
    ranks = {'2' : '2' , '3' : '3' , '4' : '4' , '5' : '5' , '6' : '6' , '7' : '7' , '8' : '8' , '9' : '9' , '10' : '10' , 'J' : '11' , 'Q' : '12' , 'K' : '13' , 'A' : '12'}
    suites = ['H', 'C', 'D', 'S']
    deck = []
    for rank in ranks:
        for suite in suites:
            deck.append(create_card(rank, suite))
    return deck

def shuffle(deck:list[dict]):
    for run in range(1000):
        index1 = random.randrange(len(deck))
        index2 = random.randrange(len(deck))
        if index1 != index2:
            deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck






