"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт, где на первом месте номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""
import random

deck = [str(x)+y for x in range(6,11) for y in [" of Spades"," of Hearts"," of Clubs"," of Diamonds"]] + [str(x)+y for x in  ["King","Queen","Jack","Ace"] for y in [" of Spades"," of Hearts"," of Clubs"," of Diamonds"]]

print("Your card - ", random.choice(deck))
