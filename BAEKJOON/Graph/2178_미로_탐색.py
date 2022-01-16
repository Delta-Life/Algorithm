#https://www.acmicpc.net/problem/2178

from collections import deque

def BFS(graph, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=M or ny < 0 or ny >= N:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x]+1
                queue.append((nx, ny))
    
    return graph[-1][-1]

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

print(BFS(graph, N, M))