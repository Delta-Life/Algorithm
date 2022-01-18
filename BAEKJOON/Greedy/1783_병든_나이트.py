# https://www.acmicpc.net/problem/1783

def greedy_knight(N, M):
    if N == 1:
        return 1
    elif N == 2:
        return min(4, (M-1)//2+1)
    elif M <= 6:
        return min(4, M)
    else:
        return M - 2

N, M = map(int, input().split())

print(greedy_knight(N, M))
