# https://www.acmicpc.net/problem/1753

import heapq

def dijkstra(graph, start, v):
    distance = [10 ** 10] * (v+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    distance = [d if d != 10 ** 10 else "INF" for d in distance]
    return distance[1:]

graph = {}
v, e = map(int, input().split())
start = int(input())

for i in range(1, v+1):
    graph[i] = []

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
print("\n".join(map(str, dijkstra(graph, start, v))))
