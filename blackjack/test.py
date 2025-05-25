import random

class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"Card with {self.rank["rank"]} and suit of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["hearts", "diamonds", "clubs", "spades"]

        ranks = [ 
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank)) # Create a card object for each suit and rank combination and
                # add to the self.cards list as an object of Card class 
                # which can be accessed by self.cards with the index of the object in the self.cards list


    def shuffle(self):
            if len(self.cards) > 1:
                random.shuffle(self.cards)



    def deal(self, number): # Can be called with number you want to deal from the deck
            # and returns the cards_out list and add to the self.card_hand list in the Hand class
            cards_out = []  # Initialize an empty list to hold the dealt cards
            for i in range(number):
                if len(self.cards) > 0:  # Check if there are cards left in the deck
                    # Pop a random last card from the self.cards list according to the number passed to the deal function
                    # and add it to the  cards_out list
                    card_remove = self.cards.pop()
                    cards_out.append(card_remove)
            return cards_out
    
class Hand:
    def __init__(self,dealer = False):
        self.card_hand = []  # Initialize an empty list to hold the cards in the hand
        self.value = 0  # Initialize the value of the hand to 0
        self.dealer = dealer # Set the dealer flag to indicate if this is a dealer's hand

    def add_card(self, card_list):
        self.card_hand.extend(card_list) # Add the cards to the hand by calling dealer's function 
                                         # with number of cards to be added and
                                         # the dealer function is the  parameter as card_list

    def calculate_value(self):
        self.value = 0 # Reset the value to 0 before calculating
        has_ace = False

        for card in self.card_hand:
            card_value = int(card.rank["value"]) # Get the value of the card
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.card_hand): # Enumerate the card_hand list to get the index and card object
            if self.dealer and index == 0 \
            and not show_all_dealer_cards and not self.is_blackjack():
            # If the hand is a dealer's hand and the index is 0(the first card of dealer)
            # and show_all_dealer_cards is False 
            # (at the the end of the game, it will be True and the dealer's hand will be shown)
            # and wherether your hand is a blackjack or not (if it is a blackjack , the dealer's hand will be shown and you win)
            # then print the card as hidden card
            # else print the card as it is
                print("Hidden Card")
            else:
                print(card) # Print the card object from Card class which return string

        if not self.dealer:
            print(f"Value of your hand is {self.get_value()}")
        else:
            print()





class Game:
    def play (self):
        game_number = 0
        gameToPlay = 0
        
        while gameToPlay <= 0:
            try:
                gameToPlay = int(input("How many games do you want to play?\n"))
            except:
                print("Please enter a valid number.")

        while game_number < gameToPlay:
            game_number += 1
            print(f"\nGame {game_number} of {gameToPlay}")

            deck = Deck() # Create a new deck of cards
            deck.shuffle() # Shuffle the deck
            player_hand = Hand()     # Create a new hand for the player
            dealer_hand = Hand(dealer=True) # Create a new hand for the dealer
            for i in range(2): # Deal 1 card to each player and dealer for two times
                player_hand.add_card(deck.deal(1))  # Deal 1 cards to the player
                dealer_hand.add_card(deck.deal(1))  # Deal 1 cards to the dealer

            print()
            print("*" * 30)


            print (f"Game {game_number} of {gameToPlay}")
            print("*" * 30)

            player_hand.display()
            dealer_hand.display()

      

            if self.check_winner(player_hand, dealer_hand):
                continue # If there is a winner, continue to the next game

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Do you want to hit or stand? (h/s): ").lower()
                print()
                while choice not in ["h", "s","hit", "stand"]:
                    choice = input("Please enter a valid choice (h/s): ").lower()
                    print()
                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()


            if self.check_winner(player_hand, dealer_hand):
                continue # If there is a winner, continue to the next game

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17: # Dealer must hit until they reach higher than 17
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)
            print(f"Value of dealer's hand is {dealer_hand_value}")

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results:")
            print("Your hand:",player_hand_value)
            print("Dealer's hand:",dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)
        
        print("\nThanks for playing!")
        print("Goodbye!")

                

    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted! Dealer wins.")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted! You win.")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both you and the dealer have blackjack! It's a tie.")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack! You win.")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack! Dealer wins.")
                return True
            
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() < dealer_hand.get_value():
                print("Dealer wins!")
            else:
                print("It's a tie!")
            return True
        # If none of the above conditions are met, return False to indicate that the game is still ongoing
        
        return False     

g = Game()
g.play()

