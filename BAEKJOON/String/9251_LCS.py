'''
LCS Algorithm

https://www.acmicpc.net/problem/9251
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''

def LCS(str1, str2):
    cost = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j], cost[i][j-1], cost[i-1][j-1]+1 if str1[j-1]==str2[i-1] else cost[i-1][j-1])
    
    return cost[-1][-1]

str1 = input().rstrip()
str2 = input().rstrip()

print(LCS(str1, str2))