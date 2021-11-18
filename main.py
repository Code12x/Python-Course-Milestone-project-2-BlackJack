import time

from Deck import Deck
from Player import Player

# Get player information
name = input("What is your name? ")

dealer = Player("Dealer")
player = Player(name)

flag = False
while not flag:
    try:
        bet_amount = int(input("How much would you like to wager? "))

    except:
        print("There was an error with your input. Please try again.")

    else:
        flag = True

deck = Deck()
deck.shuffle()

# Deal the initial cards
for x in range(2):
    player.add_card(deck.remove_card())

for x in range(2):
    dealer.add_card(deck.remove_card())


def print_hands(dealer_turn=False):
    if dealer_turn == False:
        print("\n\nThe dealer's hand:\n\tBLOCKED CARD")
        [print("\t", card, sep='') for card in dealer.get_hand() if dealer.get_hand().index(card) > 0]

    else:
        print("\n\nThe dealer's hand:")
        [print("\t", card, sep='') for card in dealer.get_hand()]

    print("\n\nYour Hand:")
    [print("\t", card, sep='') for card in player.get_hand()]


# Start of the game loop
# Player's Turn
players_turn = True
while players_turn:

    print_hands()

    is_input_an_option = False
    while not is_input_an_option:

        choice = input("\nWhat would you like to do next? [h]it or [s]tay: ")

        if choice.lower() == 'h' or choice.lower() == 's':
            is_input_an_option = True
        else:
            print("There was an error with your input. Please try again.")

    if choice == 's' or len(deck.get_cards()) <= (len(deck.get_cards()) / 2):
        players_turn = False
        continue

    player.add_card(deck.remove_card())

# Dealer's Turn
print("It is now the dealer's turn...")

dealers_turn = True
while dealers_turn:

    # Pre-round setup
    time.sleep(1)
    print_hands(dealer_turn=True)

    # Hand value
    dealer_hand_value = dealer.get_hand_value()

    # Hit or Stay logic
    if dealer_hand_value > 17:
        dealers_turn = False
        continue

    dealer.add_card(deck.remove_card())


# Evaluate the points to see who won
def winner(winner):
    print(f"{winner.get_name()} won!")


def tie():
    print("Its a tie!")


player_points = player.get_hand_value()
dealer_points = dealer.get_hand_value()

print("\n\n")
print(f"{player.get_name()} had {player_points} points.")
print(f"{dealer.get_name()} had {dealer_points} points.")

# Calculate who won
if player_points > 21 and dealer_points > 21:
    tie()

elif player_points == 21:
    if dealer_points == 21:
        tie()
    else:
        winner(player)
elif player_points > 21:
    winner(dealer)

elif dealer_points == 21:
    winner(dealer)
elif dealer_points > 21:
    winner(player)

elif player_points == dealer_points:
    tie()
elif player_points > dealer_points:
    winner(player)
elif dealer_points > player_points:
    winner(dealer)
