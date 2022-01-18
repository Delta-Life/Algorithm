# https://www.acmicpc.net/problem/2573

from collections import deque

def bingsan(height_table, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def BFS(start):
        queue = deque()
        queue.append(start)
        melting = []
        visited = [[False] * M for _ in range(N)]
        visited[start[1]][start[0]] = True

        while queue:
            x, y = queue.popleft()
            count = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if height_table[ny][nx] == 0:
                    count += 1
                elif not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                if nx < 0 or nx >=M or ny < 0 or ny >= N:
                    continue
            melting.append((x, y, height_table[y][x]-count if height_table[y][x] > count else 0))

        return melting

    year = 0
    while True:
        loaf = 0
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if height_table[i][j] != 0 and not visited[i][j]:
                    # print(i, j)
                    loaf += 1
                    melting = BFS((j, i))
                    for x, y, height in melting:
                        height_table[y][x] = height
                        visited[y][x] = True

        if loaf > 1:
            return year
        elif loaf == 0:
            return 0
        year += 1

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

print(bingsan(graph, N, M))