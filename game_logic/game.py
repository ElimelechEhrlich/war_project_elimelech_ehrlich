import utils.deck

def create_player(name:str='AI'):
    hand = []
    won_pile = []
    print ({"name":name,"hand":[],"won_pile":[]})


def init_game():
    Current_deck = [deck.shuffle(deck.create_deck())]
    player1 = create_player('eli')['hend'].append[Current_deck[0:26]]
    player2 = create_player()['hend'].append[Current_deck[26:-1]]
    return  {"deck": Current_deck ,"player_1": player1,"player_2": player2}

def play_round(player_1: dict, player_2: dict):
    Corrent_game = init_game()
    hend_of_player1 = Corrent_game['player_1'['hend']]
    hend_of_player2 = Corrent_game['player_2'['hend']]
    Compared = deck.compare_cards(hend_of_player1[-1], hend_of_player2[-1])
    if  Compared == 'p1':
        print ('P1 Winner!!!')
        Corrent_game['player_1'['won_pile']].append[hend_of_player1.pop[-1]]
    elif  Compared == 'p2':
        print ('P2 Winner!!!')
        Corrent_game['player_2'['won_pile']].append[hend_of_player2.pop[-1]]
    print ('by hend p1: ',len(hend_of_player1))
    print ('by hend p1: ',len(hend_of_player2))

