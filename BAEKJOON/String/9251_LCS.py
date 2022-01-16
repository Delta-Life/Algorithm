#https://www.acmicpc.net/problem/9251

def LCS(str1, str2):
    cost = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j], cost[i][j-1], cost[i-1][j-1]+1 if str1[j-1]==str2[i-1] else cost[i-1][j-1])
    
    return cost[-1][-1]

str1 = input().rstrip()
str2 = input().rstrip()

print(LCS(str1, str2))