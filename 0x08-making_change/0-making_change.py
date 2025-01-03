#!/usr/bin/python3
""""""


def makeChange(coins, total):
    """"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        count = total // coin
        num_coins += count
        total -= count * coin
    if total != 0:
        return -1
    return num_coins