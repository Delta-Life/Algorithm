# https://www.acmicpc.net/problem/1238

import heapq

def party(graph, party, n):
    result = 0
    def dijkstra(start):
        distance = [10 ** 10] * (n+1)
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
        return distance
    
    for i in range(1, n+1):
        result = max(result, dijkstra(party)[i] + dijkstra(i)[party])
    return result

graph = {}
n, m, x = map(int, input().split())

for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
print(party(graph, x, n))