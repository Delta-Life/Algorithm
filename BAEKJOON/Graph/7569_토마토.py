# https://www.acmicpc.net/problem/7569

from collections import deque

def tomato(tomato_box):
    H, N, M = len(tomato_box), len(tomato_box[0]), len(tomato_box[0][0])
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_box[i][j][k] == 1:
                    queue.append((k, j, i))
    
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx >= 0 and M > nx and ny >= 0 and N > ny and nz >= 0 and H > nz and tomato_box[nz][ny][nx] == 0:
                tomato_box[nz][ny][nx] = tomato_box[z][y][x] + 1
                queue.append((nx, ny, nz))
    
    max_days = 0
    for i in range(H):
        max_days = max(max_days, max(map(max, tomato_box[i])))
        for j in range(N):
            if 0 in tomato_box[i][j]:
                return -1

    return max_days - 1

M, N, H = map(int, input().split())
tomato_box = [[0] * N for _ in range(H)]

for i in range(N*H):
    tomato_box[i//N][i%N] = list(map(int, input().split()))

print(tomato(tomato_box))