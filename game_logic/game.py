
from utils import deck

def create_player(name:str='AI'):
    hand = []
    won_pile = []
    return ({"name":name,"hand":[],"won_pile":[]})


def init_game():
    Current_deck = [deck.shuffle(deck.create_deck())]
    player1 = create_player('eli')
    player2 = create_player()
    hend_of_player1 = player1['hand']
    hend_of_player2 = player2['hand']
    hend_of_player1.extend(Current_deck[0:26])
    hend_of_player2.extend(Current_deck[26:-1])
    return  {"deck": Current_deck ,"player_1": player1 ,"player_2": player1}

def play_round(player_1: dict, player_2: dict):
    hend_of_player1 = player_1['hand']
    hend_of_player2 = player_2['hand']
    won_pile_of_player1 = player_1['won_pile']
    won_pile_of_player2 = player_2['won_pile']
    Compared = deck.compare_cards(hend_of_player1[-1], hend_of_player2[-1])
    while (len(hend_of_player1) > 0) and (len(hend_of_player2) > 0):
        if  Compared == 'p1':
            print ('P1 Winner!!!')
            won_pile_of_player1.extenb(hend_of_player1.pop(-1))
            won_pile_of_player1.extend(hend_of_player2.pop(-1))
        elif  Compared == 'p2':
            print ('P2 Winner!!!')
            won_pile_of_player2.extend(hend_of_player2.pop(hend_of_player2[-1]))
            won_pile_of_player2.extend(hend_of_player1.pop(hend_of_player1[-1]))
        else:
            pass
        print ('by hend p1:', len(hend_of_player1))
        print ('by hend p2:', len(hend_of_player2))
        print ('by won_pile p1:', len(hend_of_player1))
        print ('by won_pile p2:', len(hend_of_player2))
    return
        

