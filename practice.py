import random

# List of possible options
colors = ["blue", "red", "yellow", "green"]
special_cards_with_color = ["skip", "reverse", "draw2"]
special_cards_without_color = ["draw4", "changeColor"]  # Wild cards

# Predefined UNO deck with duplicates
def create_uno_deck():
    deck = []
    
    # Add number cards
    for color in colors:
        # One "0" per color
        deck.append({color: 0})
        # Two of each number 1-9 per color
        for num in range(1, 10):
            deck.append({color: num})
            deck.append({color: num})

    # Add action cards (Skip, Reverse, Draw 2)
    for color in colors:
        for special in special_cards_with_color:
            deck.append({color: special})
            deck.append({color: special})

    # Add wild cards (Wild and Wild Draw 4)
    for _ in range(4):
        deck.append({"special card": "draw4"})
        deck.append({"special card": "changeColor"})

    return deck

# Initialize the deck and shuffle it
uno_deck = create_uno_deck()
random.shuffle(uno_deck)

# Initialize counters
cards_counter = len(uno_deck)  # Total number of cards in the UNO deck
used_cards = []  # List to track used cards

# Function to generate a random card (now draws from the shuffled deck)
def random_card():
    global cards_counter, uno_deck  # Use global variables to track total cards and the deck

    if cards_counter <= 0:
        return "No more cards available"

    # Draw the top card from the deck
    drawn_card = uno_deck.pop(0)  # Pop the first card from the shuffled deck
    used_cards.append(drawn_card)  # Track used cards
    cards_counter -= 1  # Decrease the card counter
    return drawn_card



#Generates a list of 7 cards 
def random_cards_list():
    cards_list = []
    for i in range(7):
        cards_list.append(random_card())
    return cards_list

#Gets the player name
def get_player_details():
    player_name = input("Please enter your name: ")
    return player_name
print("""
    ************
    WELCOME TO UNO!
    ************
    
      """)
# print("************")
# print("WELCOME TO UNO!")
# print("************")
# print("            ")

number_of_players = 1

players_in_game = []



while True:
        try:
            # Prompt the user to start the game (assuming you want some input before generating players)
            computer_players = input("Enter 'start' to generate computer players: ").strip().lower()
            
            if computer_players == "start":
                print("\nGenerating computer players...")
                
                # Randomly decide how many computer players to create (between 2 and 6)
                computer_players_count = random.randint(2, 7)
                
                # List of possible names for the computer players
                genericNames_list = ["Jack", "Jabu", "Tumisho", "Nkosi", "Kudzai", "Thami", "Nolo", "Jacob", "Joseph", "Ruth", "Aliyah"]
                
                # Check if we have enough names to assign unique names to the players
                if computer_players_count > len(genericNames_list):
                    raise ValueError("Not enough unique names available for the number of computer players requested.")
                
                # Generate profiles for each computer player
                players_in_game = []  # Assuming this list is used to store players
                for i in range(computer_players_count):
                    # Pick a random name and remove it to avoid duplicates
                    computer_name = random.choice(genericNames_list)
                    genericNames_list.remove(computer_name)
                    
                    # Assuming random_cards_list() returns a list of cards for the player
                    profile = [computer_name, True, random_cards_list(),True]  
                    players_in_game.append(profile)
                
                # Print computer players' names
                print("\nComputer players added:")
                for player in players_in_game:
                    print(f"Computer: {player[0]}")
                
                break  # Exit the loop after successfully generating players
            
            else:
                print("Please enter 'start' to proceed.")
        
        # Handle specific errors
        except NameError as ne:
            print(f"Error: A variable is not defined - {ne}.")
        
        except ValueError as ve:
            print(f"Value Error: {ve}.")
        
        except TypeError as te:
            print(f"Type Error: {te}. Please check if the input types are correct.")
        
        # Catch any other unexpected error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        finally:
            print("Attempt completed.\n")



# Loop to create profiles for each player
for i in range(number_of_players):
    profile = [get_player_details(), True, random_cards_list(),True]  # Player 1 starts
    players_in_game.append(profile)

# Creates a draw pile using a list
draw_pile = []

is_reverse = False
# Generates the starting card, ensuring it is not a special card
def generate_starting_card():
    while True:
        starting_card = random_card()
        
        # Ensure that it's not a special card, skip, reverse, draw2, draw4, or changeColor
        if (
            "special card" not in starting_card and
            "skip" not in starting_card.values() and
            "reverse" not in starting_card.values() and
            "draw2" not in starting_card.values() and
            "draw4" not in starting_card.values() and
            "changeColor" not in starting_card.values()
        ):
            return starting_card


# Create the starting card
starting_card = generate_starting_card()

# Creates a discarded pile using a list
discarded_pile = []
discarded_pile.append(starting_card)


print("         ")
print(f"The starting card is {starting_card}")
print("         ")


# Main game loop
while True:

    # Use the last card in the discarded pile as the current card in play (or starting card)
    current_card = starting_card if len(discarded_pile) == 0 else discarded_pile[-1]

    if is_reverse == True:
        game_direction = -1
    else:
        game_direction = 1
    
    for player in players_in_game[::game_direction]:
            # Assign player profile to variables
            name = player[0]
            is_playerturn = player[1]
            player_cards = player[2]
            is_computer = player[3]

            if is_playerturn:
                print("            ")
                print(f"{name}, It's your turn!")

                
                try:
                    
                    if is_computer == True:
                        player_choice = random.randint(1,7)
                        selected_index = player_choice - 1
                    else:
                        for card in player_cards:
                            print(card)
                        # Ask the player to select a card to play
                        player_choice = input(f"Choose a card to play from {len(player_cards)} options (please enter a number): ")
                        selected_index = int(player_choice) - 1

                    if selected_index < 0 or selected_index >= len(player_cards):
                        raise IndexError

                    selected_card = player_cards[selected_index]

                    # Print the card played
                    print("            ")
                    print(f"{name} played {selected_card}")
                    print("            ")

                # Rule Enforcement: Compare the selected card to the current card in play
                    selected_card_color = list(selected_card.keys())[0]  # Get the color or "special card"
                    selected_card_value = selected_card[selected_card_color]  # Get the value (number or special)

                    current_card_color = list(current_card.keys())[0]
                    current_card_value = current_card[current_card_color]
                     

            

                    # Rule: Check if the selected card matches the current card's color or value
                    if selected_card_color == current_card_color or selected_card_value == current_card_value:
                        print(f"Valid play! {selected_card} matches the current card {current_card}")

                        # Move the card to the discarded pile and remove it from the player's hand
                        discarded_pile.append(selected_card)
                        player_cards.pop(selected_index)

                        print(f"The discarded pile: {discarded_pile}")
                        print(f"The total number of cards in the discarded pile: {len(discarded_pile)}")
                        break

                    # Check if the card is a "changeColor" card
                    if selected_card_value == "changeColor":
                        print("A changeColor card was played!")
                            
                        # Ask the player for a new color, ensuring it's a valid color
                        while True:
                            new_color = input("Please choose a new color (blue, red, yellow, green): ").lower()
                            if new_color in colors:
                                print(f"The color has been changed to {new_color}")
                                    
                                # Change the current card to reflect the new color, keeping the "changeColor" value
                                current_card = {new_color: "changeColor"}
                                discarded_pile[-1] = current_card  # Update the last card in the discarded pile
                               
                                break
                            else:
                                print("Invalid color choice. Please choose again.")
                   
                            
                        


                    # Check if the card is a "skip" card
                    if selected_card_value == "skip":
                        # Find the index of the current player
                        current_player_index = players_in_game.index(player)

                        # Calculate the next player index (wrap around to 0 if it's the last player)
                        next_player_index = (current_player_index + 1) % len(players_in_game)

                        # Set the next player's turn flag to False to skip their turn
                        players_in_game[next_player_index][1] = False
                        print(f"{players_in_game[next_player_index][0]} has been skipped!")

                        # Move to the player after the skipped one (next-next player)
                        following_player_index = (next_player_index + 1) % len(players_in_game)
                        players_in_game[following_player_index][1] = True  # This player gets the next turn


                # Check if the card is a "draw2" card
                    if selected_card_value == "draw2":
                        print("A draw2 card was played!")
                        current_player_index = players_in_game.index(player)

                        # Calculate the next player index (wrap around if needed)
                        next_player_index = (current_player_index + 1) % len(players_in_game)
                        next_player = players_in_game[next_player_index]
                        next_players_deck = next_player[2]  # Get next player's deck (third element of profile)

                        print(f"{next_player[0]} must pick up 2 cards!")
                        
                        # Append two random cards to the next player's deck
                        for i in range(2):
                            next_players_deck.append(random_card())

                        print(f"{next_player[0]}'s new deck has {len(next_players_deck)} cards")

                    # Check if the card is a "draw4" card
                    if selected_card_value == "draw4":
                        print("A draw4 card was played!")
                        current_player_index = players_in_game.index(player)

                        # Calculate the next player index (wrap around if needed)
                        next_player_index = (current_player_index + 1) % len(players_in_game)
                        next_player = players_in_game[next_player_index]
                        next_players_deck = next_player[2]
                        player_cards.pop(selected_index)

                        print(f"{next_player[0]} must pick up 4 cards!")

                        # Append four random cards to the next player's deck
                        for i in range(4):
                            next_players_deck.append(random_card())

                        print(f"{next_player[0]}'s new deck has {len(next_players_deck)} cards")

                    
                     

                    # Check if the card is a "reverse" card
                    if selected_card_value == "reverse":
                        print("A reverse card was played!")
                        print("The order was reversed!")
                        is_reverse = True
                        player_cards.pop(selected_index)

                        
                    else:
                        print(f"Invalid play! {selected_card} does not match the current card {current_card}")
                        continue  # Let the player choose another card


                except (ValueError, IndexError):
                    print("Invalid choice! Please choose a number in the correct range.")

               

                if is_reverse == True:
                    # Find the next player
                    next_player_index = (players_in_game.index(player) - 1) % len(players_in_game)
                    break
                else:
                    next_player_index = (players_in_game.index(player) - 1) % len(players_in_game)

                # If the next player was skipped, set their turn flag to False and move to the following player
                while players_in_game[next_player_index][1] == False:
                    
                    print(f"{players_in_game[next_player_index][0]} was skipped.")
                    
                    # Move to the following player after the skipped one
                    next_player_index = (next_player_index + 1) % len(players_in_game)

                # Now assign the turn to the next player who is not skipped
                players_in_game[next_player_index][1] = True


        # Check if any player has won
    for player in players_in_game:
            if len(player[2]) == 0:
                break
