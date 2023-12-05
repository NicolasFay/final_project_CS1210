'''
Joseph Donovan & Nicolas Fay
UVM
CS 1210
11/2/2023
'''

import random
import pyfiglet

from colorama import Fore

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9'
    , '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
CARD_VALUES = {}


# Creates deck of cards and returns as list object
def createdeck():
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


# Deals list object into 2 even piles
def deal(deck):
    stack1 = []
    stack2 = []
    while deck:
        stack1.append(deck.pop(-1))
        stack2.append(deck.pop(-1))
    return stack1, stack2


# Used to decide winner between cards of tied value
def war(stack1, stack2):
    print(Fore.MAGENTA + pyfiglet.figlet_format("WAR!") + Fore.RESET)

    warpile1 = []
    warpile2 = []
    winnercards = []
    for i in range(3):
        if not stack1:
            return stack1, stack2
        if stack1:
            winnercards.append(stack1[-1])
            warpile1.append(CARD_VALUES[stack1.pop(-1)])
        if not stack2:
            return stack1, stack2
        if stack2:
            winnercards.append(stack2[-1])
            warpile2.append(CARD_VALUES[stack2.pop(-1)])
    print("Stack 1 cards:")
    for i in range(0, len(winnercards), 2):
        print(winnercards[i])
    print("\nStack 2 cards:")
    for i in range(1, len(winnercards), 2):
        print(winnercards[i])
    print("\n")
    if sum(warpile1) > sum(warpile2):
        while winnercards:
            stack1.insert(0, winnercards.pop(-1))
        print("Stack 1 wins\n")
    if sum(warpile1) < sum(warpile2):
        while winnercards:
            stack2.insert(0, winnercards.pop(-1))
        print("Stack 2 wins\n")
    return stack1, stack2


if __name__ == "__main__":
    print(colorama.Fore.MAGENTA + pyfiglet.figlet_format("WAR GAME") + colorama.Fore.RESET)
    print("Press enter to draw a card.\n")
    play = 'y'
    while play == 'y':
        stack1, stack2 = deal(createdeck(RANKS, SUITS))

        print("Welcome to War")
        print(Fore.MAGENTA + pyfiglet.figlet_format("WAR GAME") + Fore.RESET)

        while stack1 and stack2:
            print(Fore.BLUE + f"You:{len(stack1)}" + Fore.RESET, end = '')
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
        play = input("Play again? y/n ")
        while play not in ('y', 'n'):
            play = input("Play again? y/n ")
