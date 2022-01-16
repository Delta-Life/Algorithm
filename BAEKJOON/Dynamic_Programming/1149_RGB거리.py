#https://www.acmicpc.net/problem/1149

def rgb_distance(num, rgb_cost):
    cost = [[0, 0, 0] for _ in range(num+1)]
    for i in range(1, num+1):
        cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + rgb_cost[i-1][0]
        cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + rgb_cost[i-1][1]
        cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + rgb_cost[i-1][2]
    
    return min(cost[-1][i] for i in range(3))

N = int(input())
rgb_cost = []

for i in range(N):
    rgb_cost.append(list(map(int, input().split())))

print(rgb_distance(N, rgb_cost))