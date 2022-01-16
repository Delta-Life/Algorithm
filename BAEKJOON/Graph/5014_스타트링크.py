#https://www.acmicpc.net/problem/5014

from collections import deque

def elevator(F, S, G, U, D):
    floors = [0] * (F + 1)
    floors[S] = 1
    queue = deque([S])
    while queue:
        floor = queue.popleft()
        if floor == G:
            return floors[G] - 1
        if floor + U <= F and floors[floor+U] == 0:
            floors[floor+U] = floors[floor] + 1
            queue.append(floor+U)
        if floor - D > 0 and floors[floor-D] == 0:
            floors[floor-D] = floors[floor] + 1
            queue.append(floor-D)

    return 'use the stairs'

F, S, G, U, D = map(int, input().split())

print(elevator(F, S, G, U, D))