n = int(input())
m = int(input())

graph = [[10 ** 10] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
     
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == 10 ** 10 or a == b:
            graph[a][b] = 0

for cost in graph[1:]:
    print(" ".join(map(str, cost[1:])))