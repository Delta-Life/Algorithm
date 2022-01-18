def num_of_cases(coins, k):
    cases = [0] * (k+1)
    cases[0] = 1

    for coin in coins:
        for i in range(coin, k+1):
            if 0 <= i - coin:
                cases[i] += cases[i-coin]

    return cases[k]

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(num_of_cases(coins, k))
