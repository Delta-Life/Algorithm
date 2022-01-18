# https://www.acmicpc.net/problem/2468

from collections import deque

def get_num_of_safe_area(graph, N):
    def BFS(graph, start):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()
        queue.append(start)

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >=N or ny < 0 or ny >= N:
                    continue

                if graph[ny][nx] == True:
                    continue

                if graph[ny][nx] == False:
                    graph[ny][nx] = True
                    queue.append((nx, ny))

    max_safe_area = 1
    for k in range(max(map(max, graph))):
        sink_table = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if graph[i][j] <= k:
                    sink_table[i][j] = True

        safe_area = 0
        for i in range(N):
            for j in range(N):
                if sink_table[i][j] == False:
                    sink_table[i][j] = True
                    safe_area += 1
                    BFS(sink_table, (j, i))

        max_safe_area = max(max_safe_area, safe_area)
    
    return max_safe_area

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

print(get_num_of_safe_area(graph, N))