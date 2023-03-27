import random
def generate_deck(_suits,_cards):
    random.seed(0)
    n=0
    deck = [(i,j) for i in _suits for j in _cards]
    random.shuffle(deck)
    while True:
        yield deck[n]
        n += 1
        if n== 52:
            random.shuffle(deck)
            n=0

suits = ["Spades", "Heart", "Clubs", "Diamonds"]
cards =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
shuffled_deck = generate_deck(suits,cards)
def get_next_card():
    return next(shuffled_deck)

def card_value(card):
    if card[1] in ['A','J','Q']:
        return 10
    elif card[1] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(card[1])
    elif card[1] in ['K']:
        if card[0] in ['Hearts', 'Diamonds']:
            return 1
        else:
            return 11
    else:
        return None
i=0
while i <55:
    x = get_next_card()
    print(x)
    print(card_value(x))
    i += 1

