import random

def create_card(rank:str,suite:str):
    ranks = {'2' : '2' , '3' : '3' , '4' : '4' , '5' : '5' , '6' : '6' , '7' : '7' , '8' : '8' , '9' : '9' , '10' : '10' , '11' : 'J' , '12' : 'Q' , '13' : 'K' , '14' : 'A'}
    suites = ['H', 'C', 'D', 'S']
    for letter in ranks:
        if  letter == rank:
            for i in suites:
                if i == suite:
                    return ({'rank': rank, 'suite': suite, 'value': letter})
            return ('Incorrect suite input')
    return ('Incorrect rank input')

def compare_cards(p1_card:dict, p2_card:dict):
    try:
        if p1_card['value'] > p2_card['value']:
            return ('p1')
        elif p2_card['value'] > p1_card['value']:
            return ('p2')
        elif p2_card['value'] == p1_card['value']:
            return ('WAR')
    except:
        print (f'"value" key is does not exist in Or its value is not of type number at least one of the dictionaries')
    return
                                      
def create_deck(): 
    ranks = {'2' : '2' , '3' : '3' , '4' : '4' , '5' : '5' , '6' : '6' , '7' : '7' , '8' : '8' , '9' : '9' , '10' : '10' , '11' : 'J' , '12' : 'Q' , '13' : 'K' , '14' : 'A'}
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
        if index1 == index2:
            index1 = random.randrange(len(deck))
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck






