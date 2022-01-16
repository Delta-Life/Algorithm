#https://www.acmicpc.net/problem/1697

from collections import deque


def BFS(src, dst):
    map = [0] * (10**5 + 1)
    map[src] = 1
    queue = deque([src])
    while queue and map[dst] == 0:
        cur = queue.popleft()
        for nx in (cur + 1, cur - 1, cur * 2):
            if 0 <= nx <= len(map) - 1 and map[nx] == 0:
                map[nx] = map[cur] + 1
                queue.append(nx)
    return map[dst] - 1

src, dst = map(int, input().split())

print(BFS(src, dst))