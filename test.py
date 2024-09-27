import random
# Create a list of colors
colors = ["red", "yellow", "green", "blue"]

# Create a list of numbers
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Create a list of action cards
action_cards = ["reverse", "skip", "draw_two"]

# Create a list of wild cards
wild_cards = ["wild", "wild_draw_four"]

# Create a new deck
deck = []

# Add number cards to the deck
for color in colors:
    for number in numbers:
        deck.append([color, number])

# Add action cards to the deck
for color in colors:
    for action_card in action_cards:
        deck.append([color, action_card])

# Add wild cards to the deck
for i in range(4):
    deck.append(wild_cards[0])
    deck.append(wild_cards[1])

# Shuffle the deck
random.shuffle(deck)

# Create a player's hand
player_1 = []

for card in range(7):
    player_1.append(deck.pop(0))

print(player_1)

