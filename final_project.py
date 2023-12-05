'''
Joseph Donovan & Nicolas Fay
UVM
CS 1210
11/2/2023
'''

import random
import time
import pyfiglet

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


def war(stack1, stack2):
    print(pyfiglet.figlet_format("WAR"))
    warpile1 = []
    warpile2 = []
    winnercards = []
    for i in range(3):
        if not stack1:
            return stack1, stack2
        elif stack1:
            winnercards.append(stack1[-1])
            warpile1.append(CARD_VALUES[stack1.pop(-1)])
        if not stack2:
            return stack1, stack2
        elif stack2:
            winnercards.append(stack2[-1])
            warpile2.append(CARD_VALUES[stack2.pop(-1)])
    if sum(warpile1) > sum(warpile2):
        while winnercards:
            stack1.insert(0, winnercards.pop(-1))
        print("Stack 1 wins")
    if sum(warpile1) < sum(warpile2):
        while winnercards:
            stack2.insert(0, winnercards.pop(-1))
        print("Stack 2 wins")
    return stack1, stack2


if __name__ == "__main__":
    print("Press enter to draw a card.")
    play = 'y'
    while play == 'y':
        stack1, stack2 = deal(createdeck(RANKS, SUITS))
        print(stack1)
        print(stack2)

        while stack1 and stack2:
            print(f"{stack1[-1]} VS {stack2[-1]}")
            input("")
            if CARD_VALUES[stack1[-1]] > CARD_VALUES[stack2[-1]]:
                stack1.insert(0, stack2.pop(-1))
                stack1.insert(0, stack1.pop(-1))
            elif CARD_VALUES[stack1[-1]] < CARD_VALUES[stack2[-1]]:
                stack2.insert(0, stack1.pop(-1))
                stack2.insert(0, stack2.pop(-1))
            else:
                stack1, stack2 = war(stack1, stack2)
            # time.sleep(1)
        if stack1:
            print("Stack 1 wins the game")
        elif stack2:
            print("Stack 2 wins the game")
        print(stack1)
        print(stack2)
        play = input("Play again? y/n ")
        while play != 'y' and play != 'n':
            play = input("Play again? y/n ")




