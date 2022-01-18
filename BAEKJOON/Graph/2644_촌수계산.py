# https://www.acmicpc.net/problem/2644

from collections import deque, defaultdict

def BFS(graph, src, dst, n):
    count = [0] * (n+1)
    queue = deque()
    queue.append(src)
    visited = [src]

    while queue and dst not in queue:
        node = queue.popleft()
        for value in graph[node]:
            if value not in visited:
                count[value] = count[node] + 1
                visited.append(value)
                queue.append(value)
    
    return count[dst] if count[dst] != 0 else -1

n = int(input())
src, dst = map(int, input().split())
edge_num = int(input())
graph = defaultdict(list)

for _ in range(edge_num):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

print(BFS(graph, src, dst, n))