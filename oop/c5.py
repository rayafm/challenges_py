# Assignment
# Finish the DeckOfCards class. The SUITS and RANKS of each card have been provided for you as class variables. 
# You won't need to modify them, but you will need to use them.

# Complete the constructor:
# Initialize a private empty list called cards.
# Fill that empty list by calling the create_deck method within the constructor.
# Complete the create_deck(self) method:
# Create a (Rank, Suit) tuple for all 52 cards in the deck and append them to the cards list.

# Order matters! The cards should be appended to the list in the following order: 
# all ranks of hearts, then diamonds, then clubs, and finally spades. 
# Within each suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).

# Complete the shuffle_deck(self) method:
# Use the random.shuffle() method (available from the random package) to shuffle the cards in the deck.
# Complete the deal_card(self) method:
# .pop() the first card off the top of the deck (top of the deck is the end of the list) and return it. 
# If there are no cards left in the deck the method should instead return None. 

import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                tp_ranksuit = (rank, suit)
                self.__cards.append(tp_ranksuit)

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        else:
            return self.__cards.pop()

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"