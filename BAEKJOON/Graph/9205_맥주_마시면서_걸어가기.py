# https://www.acmicpc.net/problem/9205

from collections import deque

def bfs(x0, y0, graph, x1, y1):
    queue, visited = deque(), [[x0, y0]]
    queue.append([x0, y0])
    while queue:
        x, y = queue.popleft()
        if x == x1 and y == y1:
            return "happy"
        for nx, ny in graph:
            if [nx, ny] not in visited:
                l1 = abs(nx - x) + abs(ny - y)
                if 1000 >= l1:
                    queue.append([nx, ny])
                    visited.append([nx, ny])
    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    x0, y0 = map(int, input().split())
    graph = []
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append([x, y])
    x1, y1 = map(int, input().split())
    graph.append([x1, y1])
    print(bfs(x0, y0, graph, x1, y1))