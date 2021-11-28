"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту. Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""

import random

deck = [6,7,8,9,10,2,3,4,11] * 4

random.shuffle(deck)

print('Blackjack?')
count = 0

while True:
    choice = input('Will you take the card? y/n\n')
    if choice == 'y':
        current = deck.pop()
        print('You got a card of %d' %current)
        count += current
        if count > 21:
            print('Im sorry but you lost')
            break
        elif count == 21:
            print('Congratulations, you got 21!')
            break
        else:
            print('You have %d points.' %count)
    elif choice == 'n':
        print('You have %d points and you finished the game.' %count)
        break

print('Good Bye!')