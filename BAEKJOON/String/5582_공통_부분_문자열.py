#https://www.acmicpc.net/problem/5582

def LCS(str1, str2):
    cost = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str1[j-1] == str2[i-1]:
                cost[i][j] = cost[i-1][j-1] + 1

    return max(map(max, cost))

str1 = input().rstrip()
str2 = input().rstrip()

print(LCS(str1, str2))