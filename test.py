from random import *

colors = ['red', 'yellow', 'green', 'blue']

special_cards = ['+2', 'block', 'reverse', 'wild', '+4']

deck = []
discard_deck = []

player_one = []
player_two = []
current_player = 1
skip_turn = False

# create the deck
for color in colors:
    for number in range(10):
        deck.append((color, number))
    for special in special_cards[:-1]:
        deck.append((color, special))
for _ in range(4):
    deck.append(('wild', '+4'))

# Shuffle deck
shuffle(deck)

# discard deck
first = choice(deck)
discard_deck.append(first)
deck.remove(first)

def print_card(card):
    color, value = card
    return f"{color} {value}\n"

def play():
    global deck, discard_deck, player_one, player_two, current_player, skip_turn
    
    # Deal cards to both players
    for i in range(7):
        player_one.append(deck.pop())
        player_two.append(deck.pop())
    
    def draw_card(player):
        if deck:
            player.append(deck.pop())
        else:
            print("Deck is empty! Reshuffling...")
            reshuffle_discard()

    def reshuffle_discard():
        global discard_deck, deck
        deck = discard_deck[:-1]
        discard_deck = [discard_deck[-1]]
        shuffle(deck)
    
    def player_turn(player, opponent):
        global skip_turn, current_player

        if skip_turn:
            skip_turn = False
            print(f"Player {current_player}'s turn is skipped!")
            current_player = 2 if current_player == 1 else 1
            return
        
        print(f"Top of discard pile: {print_card(discard_deck[-1])}")
        print(f"Player {current_player} cards: ", [print_card(card) for card in player])
        
        chosen_card = int(input(f"Player {current_player} pick a card (enter index or -1 to draw): "))
        
        if chosen_card == -1:
            draw_card(player)
            return

        if chosen_card >= len(player):
            print("Invalid choice!")
            return

        card = player[chosen_card]

        if (card[0] == discard_deck[-1][0] or  # Color match
            card[1] == discard_deck[-1][1] or  # Number/special match
            card[0] == 'wild'):  # Wild card

            print(f"Card played: {print_card(card)}")
            discard_deck.append(card)
            player.pop(chosen_card)
            
            # Handle special card effects
            if card[1] == '+2':
                print("Next player draws 2 cards!")
                draw_card(opponent)
                draw_card(opponent)
                current_player = 2 if current_player == 1 else 1

            elif card[1] == '+4':
                print("Next player draws 4 cards!")
                draw_card(opponent)
                draw_card(opponent)
                draw_card(opponent)
                draw_card(opponent)
                chosen_color = input("Choose a color [red, yellow, green, blue]: ").lower()
                discard_deck.append((chosen_color, 'wild'))
                current_player = 2 if current_player == 1 else 1

            elif card[1] == 'block':
                print("Next player's turn is blocked!")
                skip_turn = True

            elif card[1] == 'reverse':
                print("Turn direction reversed!")
                current_player = 2 if current_player == 1 else 1

            elif card[0] == 'wild':
                chosen_color = input("Choose a color [red, yellow, green, blue]: ").lower()
                discard_deck.append((chosen_color, 'wild'))
                current_player = 2 if current_player == 1 else 1

        else:
            print("Card does not match, draw a card!")
            draw_card(player)

    while len(player_one) > 0 and len(player_two) > 0:
        if current_player == 1:
            player_turn(player_one, player_two)
        else:
            player_turn(player_two, player_one)

        # Check for a winner
        if len(player_one) == 0:
            print("Player One wins!")
            break
        elif len(player_two) == 0:
            print("Player Two wins!")
            break
        
        current_player = 2 if current_player == 1 else 1

play()