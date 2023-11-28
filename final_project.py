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
CARD_VALUES = {}


def createdeck(ranks, suits):
    deck = []
    for i in RANKS:
        for e in SUITS:
            deck.append(f"{i} of {e}")
    num = 2
    count = 0
    for cardName in deck:
        CARD_VALUES[cardName] = num
        count += 1
        if count == 4:
            num += 1
            count = 0
    random.shuffle(deck)
    return deck


def deal(deck):
    stack1 = []
    stack2 = []
    while deck:
        stack1.append(deck.pop(-1))
        stack2.append(deck.pop(-1))
    return stack1, stack2


if __name__ == "__main__":
    stack1, stack2 = deal(createdeck(RANKS, SUITS))
    print(stack1)
    print(stack2)

    while stack1 and stack2:
        print(f"{stack1[-1]} VS {stack2[-1]}")
        if CARD_VALUES[stack1[-1]] > CARD_VALUES[stack2[-1]]:
            stack1.insert(0, stack2.pop(-1))
        elif CARD_VALUES[stack1[-1]] < CARD_VALUES[stack2[-1]]:
            stack2.insert(0, stack1.pop(-1))
        else:
            break
    print(stack1)
    print(stack2)



