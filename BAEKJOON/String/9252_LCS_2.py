#https://www.acmicpc.net/problem/9252

def LCS(str1, str2):
    cost = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]
    result = []

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j], cost[i][j-1], cost[i-1][j-1]+1 if str1[j-1]==str2[i-1] else cost[i-1][j-1])
    
    j = len(str1)
    i = len(str2)
    while cost[i][j] != 0:
        if cost[i][j] == cost[i-1][j-1]:
            i -= 1
            j -= 1
        elif cost[i][j] == cost[i][j-1]:
            j -= 1
        elif cost[i][j] == cost[i-1][j]:
            i -= 1
        elif cost[i][j] - 1 == cost[i-1][j-1]:
            i -= 1
            j -= 1
            result.append(str1[j])

    return result[::-1]

str1 = input().rstrip()
str2 = input().rstrip()

lcs = LCS(str1, str2)
print(len(lcs))
print("".join(lcs))