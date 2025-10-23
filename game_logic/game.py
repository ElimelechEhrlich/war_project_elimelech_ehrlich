from utils import deck

def create_player(name:str):
    return {"name":"","hand":[],"won_pile":[]}

def init_game():

    deck.shuffle(deck.create_deck())
    deck.play_round(deck.create_player(__name__), deck.create_player(__name__))

    return  {"deck": "<the deck dict you created, shuffled>","player_1": "<human player dict you created>","player_2": "<AI player dict you created>"}

def play_round(p1:dict,p2:dict):
    return 


