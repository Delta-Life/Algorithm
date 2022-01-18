# https://www.acmicpc.net/problem/11047

def greedy_coin(K, coins):
    count = 0

    for coin in coins[::-1]:
        count += K // coin
        K %= coin
    
    return count


N, K = map(int, input().split())
coins = [0] * N

for i in range(N):
    coins[i] = int(input())

print(greedy_coin(K, coins))