# https://www.acmicpc.net/problem/16953

def greedy_min_cal(A, B):
    count = 1
    while A != B and (B % 2 == 0 or B % 10 == 1) and B > 0:
        if B % 10 == 1:
            B //= 10
        else:
            B //= 2
        count += 1
    return count if A == B else -1


A, B = map(int, input().split())
print(greedy_min_cal(A, B))
