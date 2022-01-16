#https://www.acmicpc.net/problem/1260

from collections import deque, defaultdict

def DFS(graph, start):
    visited=[]
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for value in graph[node][::-1]:
                if value not in visited:
                    stack.append(value)
    
    return visited

def BFS(graph, start):
    queue = deque()
    queue.append(start)
    visited = [start]

    while queue:
        node = queue.popleft()
        for value in graph[node]:
            if value not in visited:
                visited.append(value)
                queue.append(value)
    
    return visited

_, edge_num, start = map(int, input().split())
graph = defaultdict(list)

for _ in range(edge_num):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for key in graph.keys():
    graph[key].sort()

print(" ".join(map(str, DFS(graph, start))))
print(" ".join(map(str, BFS(graph, start))))