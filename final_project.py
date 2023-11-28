'''
Joseph Donovan & Nicolas Fay
UVM
CS 1210
11/2/2023
'''

import random

# yo
# nick branch test
# nick brach test number 2


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Spades', 'Clubs', 'Hearts', 'Diamonds']


if __name__ == "__main__":
    deck = []
    for i in RANKS:
        for e in SUITS:
            deck.append(f"{i} of {e}")
    random.shuffle(deck)
    print(deck)