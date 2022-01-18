# https://www.acmicpc.net/problem/10844

def get_stairs_num(N):
    stairs = [[0] * 10 for _ in range(N+1)]
    stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, N+1):
        stairs[i][0] = stairs[i-1][1]
        for j in range(1, 9):
            stairs[i][j] = stairs[i-1][j-1] + stairs[i-1][j+1]
        stairs[i][9] = stairs[i-1][8]
    
    return sum(stairs[N]) % 1000000000

N = int(input())

print(get_stairs_num(N))