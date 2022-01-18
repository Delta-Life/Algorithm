# https://www.acmicpc.net/problem/1958

def get_multiple_subsequence(str1, str2, str3):
    cost = [[[0]*(len(str1)+1) for _ in range(len(str2)+1)] for _ in range(len(str3)+1)]

    for i in range(1, len(str3)+1):
        for j in range(1, len(str2)+1):
            for k in range(1, len(str1)+1):
                if str3[i-1] == str2[j-1] and str2[j-1] == str1[k-1]:
                    cost[i][j][k] = 1 + cost[i-1][j-1][k-1]
                else:
                    cost[i][j][k] = max(cost[i-1][j-1][k-1], cost[i-1][j-1][k], cost[i][j-1][k-1], cost[i-1][j][k-1], cost[i-1][j][k], cost[i][j-1][k], cost[i][j][k-1])
    return cost[-1][-1][-1]

str1 = input()
str2 = input()
str3 = input()

print(get_multiple_subsequence(str1, str2, str3))