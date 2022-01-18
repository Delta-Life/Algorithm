# https://www.acmicpc.net/problem/2606

from collections import defaultdict

def DFS(graph, start):
    visited=[]
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for value in graph[node]:
                if value not in visited:
                    stack.append(value)
    
    return visited

_ = int(input())
edge_num = int(input())
graph = defaultdict(list)

for _ in range(edge_num):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

print(len(DFS(graph, 1))-1)