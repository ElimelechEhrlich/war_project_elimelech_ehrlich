from utils import deck

def create_player(name:str='AI'):
    hand = []
    won_pile = []
    print ({"name":name,"hand":[],"won_pile":[]})


def init_game():
    Current_deck = [deck.shuffle(deck.create_deck())]
    player1 = create_player('eli')
    playet2 = create_player()
    hend_of_player1 = player1['hand']
    hend_of_player2 = player2['hand']
    cards_player1 = hend_of_player1.append[Current_deck[0:26]]
    cards_player2 = hend_of_player2.append[Current_deck[26:-1]]
    return  {"deck": Current_deck ,"player_1": cards_player1,"player_2": cards_player2}

def play_round(player_1: dict, player_2: dict):
    hend_of_player1 = player_1['hand']
    hend_of_player2 = player_2['hand']
    won_pile_of_player1 = player_1['won_pile']
    won_pile_of_player2 = player_2['won_pile']
    Compared = deck.compare_cards(hend_of_player1[-1], hend_of_player2[-1])
    if  Compared == 'p1':
        print ('P1 Winner!!!')
        won_pile_of_player1.append[hend_of_player1.pop[-1]]
    elif  Compared == 'p2':
        print ('P2 Winner!!!')
        won_pile_of_player2.append[hend_of_player2.pop[-1]]
    print ('by hend p1: ',len(hend_of_player1))
    print ('by hend p1: ',len(hend_of_player2))

