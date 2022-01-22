# https://www.acmicpc.net/problem/1167

from collections import deque, defaultdict

def bfs(start, v, graph):
    visited = [-1] * (v + 1)
    queue = deque([start])
    visited[start] = 0
    _max = 0, 0

    while queue:
        node = queue.popleft()
        for n_node, cost in graph[node]:
            if visited[n_node] == -1:
                visited[n_node] = visited[node] + cost
                queue.append(n_node)
                if _max[0] < visited[n_node]:
                    _max = visited[n_node], n_node

    return _max

v = int(input())
graph = defaultdict(list)

for _ in range(v):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

_, node = bfs(1, v, graph)
dis, _ = bfs(node, v, graph)
print(dis)