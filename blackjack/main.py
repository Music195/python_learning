import random
# This is a simple blackjack game


class Card:
    def __init__(self, suit, rank  ):
        self.suit = suit # Initialize the suit of the card
        self.rank = rank # Initialize the rank of the card
    def __str__(self):
        return f"this is card object  {self.rank['rank']} of {self.suit}" # Return a string representation of the card 

#card2 = Card("hearts", {"rank": "A", "value": 11}) # Create a card object with suit and rank
#print(card2) # Print the card object

class Desk:
    def __init__(self):
        self.cards = [] # Initialize an empty list to hold the cards
        suits = ["hearts", "diamonds", "clubs", "spades"] # Define the suits of the cards
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
        ]   # Define the ranks of the cards with their values


        for suit in suits:  # Loop through each suit
            for i in range(len(ranks)):  # Loop through each rank
                self.cards.append(Card(suit, ranks[i]))  # Create a card object and append it to the list of cards
#Start from here
    def shuffle(self):
        if len(self.cards) > 1: # Check if there are more than one card in the deck
            random.shuffle(self.cards)   # Shuffle the deck of cards

    def deal(self,number):   # Deal a specified number of cards from the deck
        cards_dealt = []    # Initialize an empty list to hold the dealt cards
        for i in range(number): # Loop through the number of cards to be dealt
            if len(self.cards) > 0:  # Check if there are cards left in the deck
                card = self.cards.pop()  # Remove a card from the deck and store it in a variable
                cards_dealt.append(card)    # Append the dealt card to the list of dealt cards

        return cards_dealt  # Return the list of dealt cards
    

    

class Hand:
    def __init__(self, dealer=False): # Initialize a hand of cards
        self.cards = [] # Initialize an empty list to hold the cards in the hand example {"rank": "A", "value": 11}
        self.value = 0 # Initialize the value of the hand to 0
        self.dealer = dealer # Initialize a flag to indicate if the hand is for the dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)  # Add the dealt cards to the hand

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards: # Loop through each card in the hand
            card_value = int(card.rank["value"]) # Get the value of the card and convert it to an integer
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21: # Check if the hand has an ace and if the value is greater than 21
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value # Calculate and return the value of the hand
    
    def is_blackjack(self):
        return self.get_value() == 21 # Check if the hand is a blackjack (21 points)
    
    def display(self):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')

        for card in self.cards: # Loop through each card in the hand
            print(card) # Print the card

        if not self.dealer:
            print("Value:", self.get_value())
        print

deck = Desk()  # Create a new deck of cards
deck.shuffle()  # Shuffle the deck of cards

hand = Hand()  # Create a new hand
hand.add_card(deck.deal(2))  # Deal 2 cards to the hand

hand.display()  # Display the hand

        

