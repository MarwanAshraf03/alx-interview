#!/usr/bin/python3
"""prime game module"""


def isWinner(x, nums):
    """helper function"""
    def sieve(n):
        """helper function"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        is_prime = sieve(n)
        prime_count = sum(is_prime[:n + 1])

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
