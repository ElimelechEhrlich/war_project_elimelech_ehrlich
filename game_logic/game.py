
from utils import deck

def create_player(name:str='AI'):
    hand = []
    won_pile = []
    return ({'name':name,'hand':[],'won_pile':[]})


def init_game():
    Current_deck = deck.shuffle(deck.create_deck())
    player1 = create_player('eli')
    player2 = create_player()
    hend_of_player1 = player1['hand']
    hend_of_player2 = player2['hand']
    hend_of_player1.extend(Current_deck[0:26])
    hend_of_player2.extend(Current_deck[26:-1])
    #print (player1)
    return  {"deck": Current_deck ,"player_1": player1 ,"player_2": player1}

def play_round(player_1: dict, player_2: dict):
    #hend_of_player1 = player_1['hand'].pop(-1)
    #hend_of_player2 = player_2['hand'].pop(-1)
    won_pile_of_player1 = player_1['won_pile']
    won_pile_of_player2 = player_2['won_pile']
    #Compared = deck.compare_cards(hend_of_player1, hend_of_player2)
    while (len(player_1['hand']) > 0) and (len(player_2['hand']) > 0):
        hend_of_player1 = player_1['hand'].pop(-1)
        hend_of_player2 = player_2['hand'].pop(-1)
        Compared = deck.compare_cards(hend_of_player1, hend_of_player2)
        if  Compared == 'p1':
            print ('P1 Winner!!!')
            won_pile_of_player1.append(hend_of_player1)
            won_pile_of_player1.append(hend_of_player2)
        elif  Compared == 'p2':
            print ('P2 Winner!!!')
            won_pile_of_player2.append(hend_of_player1)
            won_pile_of_player2.append(hend_of_player2)
        else:
            won_pile_of_player1.append(hend_of_player1)
            won_pile_of_player2.append(hend_of_player2)
        print ('by hend p1:', len(player_1['hand']))
        print ('by hend p2:', len(player_2['hand']))
        print ('by won_pile p1:', len(won_pile_of_player1))
        print ('by won_pile p2:', len(won_pile_of_player2))
        print (hend_of_player2)
    return
        

