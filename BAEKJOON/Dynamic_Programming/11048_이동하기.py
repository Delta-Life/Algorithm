# https://www.acmicpc.net/problem/11048

def get_max_candies(candy_table, n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = candy_table[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[n][m]


n, m = map(int, input().split())
candy_table = []
for i in range(n):
    candy_table.append(list(map(int, input().split())))
print(get_max_candies(candy_table, n, m))