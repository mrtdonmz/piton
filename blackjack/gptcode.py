import random

def get_next_card():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return random.choice(suits), random.choice(points)

def card_value(card):
    if card[1] == 'A':
        return 10
    elif card[1] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(card[1])
    elif card[1] in ['J', 'Q']:
        return 10
    elif card[1] == 'K':
        return 1 if card[0] in ['Hearts', 'Diamonds'] else 11

def total_value(cards):
    return sum([card_value(card) for card in cards])

sages_money = int(input("Sage's money: "))
num_games = int(input("Number of games: "))

for game in range(1, num_games + 1):
    print(f"Game {game}:")
    
    kings_cards = [get_next_card(), get_next_card()]
    sages_cards = [get_next_card(), get_next_card()]
    
    print("King's cards: (*,", kings_cards[1], ") Total value:", card_value(kings_cards[1]))
    print("Sage's cards:", sages_cards, "Total value:", total_value(sages_cards))
    
    while True:
        if total_value(sages_cards) == 21:
            sages_money += 50
            print("It is Blackking! You won!")
            break
        elif total_value(sages_cards) > 21:
            sages_money -= 50
            print("You busted! You lost!")
            break
        else:
            decision = input("Do you want to hit or stand? [H/S] ")
            if decision == 'H':
                sages_cards.append(get_next_card())
                print("Sage's cards:", sages_cards, "Total value:", total_value(sages_cards))
            elif decision == 'S':
                break

    if total_value(sages_cards) <= 21:
        print("King's cards:", kings_cards, "Total value:", total_value(kings_cards))
        while total_value(kings_cards) < 17:
            kings_cards.append(get_next_card())
            print("King's cards:", kings_cards, "Total value:", total_value(kings_cards))

        if total_value(kings_cards) > 21:
            sages_money += 50
            print("King busted! You won!")
        elif total_value(kings_cards) >= total_value(sages_cards):
            sages_money -= 50
            print("King has higher value. You lost!")
        else:
            sages_money += 50
            print("You have higher value. You won!")

print("Final money is", sages_money)