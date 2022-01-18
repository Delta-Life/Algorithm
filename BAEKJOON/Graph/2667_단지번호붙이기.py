# https://www.acmicpc.net/problem/2178

from collections import deque

def get_asc_num_of_one_loaf(graph, N):
    result = []
    def BFS(graph, start):
        count = 1
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

                if graph[ny][nx] == 0:
                    continue

                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    count += 1
                    queue.append((nx, ny))
        result.append(count)
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                graph[i][j] = 0
                BFS(graph, (j, i))
    
    return sorted(result)

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

num_of_one_loaf = get_asc_num_of_one_loaf(graph, N)
print(len(num_of_one_loaf))
print("\n".join(map(str, num_of_one_loaf)))