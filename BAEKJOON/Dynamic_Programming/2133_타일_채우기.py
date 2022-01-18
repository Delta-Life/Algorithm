# https://www.acmicpc.net/problem/2133

def get_num_of_tiles(N):
    num_of_tiles = [0] * (31)
    num_of_tiles[2] = 3
    for i in range(4, N+1, 2):
        num_of_tiles[i] =  2 + num_of_tiles[i-2] * 3 + sum(num_of_tiles[:i-2] * 2)
    return num_of_tiles[N]

N = int(input())
print(get_num_of_tiles(N))