"""
Joseph Donovan & Nicolas Fay
UVM
CS 1210
11/2/2023
"""

import random
import pyfiglet
from colorama import Fore


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
CARD_VALUES = {}
stack1 = []
stack2 = []


def createdeck():
    """Creates deck of cards and returns as list object"""
    deck = []
    for i in RANKS:
        for e in SUITS:
            deck.append(f"{i} of {e}")
    num = 2
    count = 0
    for card_name in deck:
        CARD_VALUES[card_name] = num
        count += 1
        if count == 4:
            num += 1
            count = 0
    random.shuffle(deck)
    return deck


def deal(deck):
    """Deals list object into 2 even piles"""
    stack1.clear()
    stack2.clear()
    while deck:
        stack1.append(deck.pop(-1))
        stack2.append(deck.pop(-1))
    return stack1, stack2


def war(war_stack1, war_stack2):
    """Used to decide winner between cards of tied value"""
    print(Fore.RED + pyfiglet.figlet_format("WAR!") + Fore.RESET)
    warpile1 = []
    warpile2 = []
    winnercards = []
    for i in range(3):
        if not war_stack1:
            return war_stack1, war_stack2
        if war_stack1:
            winnercards.append(war_stack1[-1])
            warpile1.append(CARD_VALUES[war_stack1.pop(-1)])
        if not war_stack2:
            return war_stack1, war_stack2
        if war_stack2:
            winnercards.append(war_stack2[-1])
            warpile2.append(CARD_VALUES[war_stack2.pop(-1)])
    print("Stack 1 cards:")
    for i in range(0, len(winnercards), 2):
        print(winnercards[i])
    print("\nStack 2 cards:")
    for i in range(1, len(winnercards), 2):
        print(winnercards[i])
    print("\n")
    if sum(warpile1) > sum(warpile2):
        while winnercards:
            war_stack1.insert(0, winnercards.pop(-1))
        print("Stack 1 wins\n")
    if sum(warpile1) < sum(warpile2):
        while winnercards:
            war_stack2.insert(0, winnercards.pop(-1))
        print("Stack 2 wins\n")
    return war_stack1, war_stack2


if __name__ == "__main__":
    print(Fore.MAGENTA + pyfiglet.figlet_format("WAR GAME") + Fore.RESET)
    print("Press enter to draw a card.\n")
    PLAY = 'y'
    while PLAY == 'y':
        stack1, stack2 = deal(createdeck())
        print("Welcome to War")
        while stack1 and stack2:
            print(Fore.BLUE + f"You:{len(stack1)}" + Fore.RESET, end='')
            print(Fore.RED + f"\tOpp:{len(stack2)}" + Fore.RESET)
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
        if stack1:
            print("Stack 1 wins the game")
        elif stack2:
            print("Stack 2 wins the game")
        print(stack1)
        print(stack2)
        PLAY = input("Play again? y/n ")
        while PLAY not in ('y', 'n'):
            PLAY = input("Play again? y/n ")
