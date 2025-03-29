import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.__rank_index = RANKS.index(rank)
        self.__suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.__rank_index == other.__rank_index
            and self.__suit_index == other.__suit_index
        )

    def __lt__(self, other):
        if self.__rank_index == other.__rank_index:
            return self.__suit_index < other.__suit_index
        else:
            return self.__rank_index < other.__rank_index

    def __gt__(self, other):
        if self.__rank_index == other.__rank_index:
            return self.__suit_index > other.__suit_index
        else:
            return self.__rank_index > other.__rank_index

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
