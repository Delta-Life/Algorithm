# https://www.acmicpc.net/problem/2217

def greedy_rope(weight_array):
    weight_array.sort()
    return max(i*(n+1) for n, i in enumerate(weight_array[::-1]))

N = int(input())
weight_array = [0] * N

for i in range(N):
    weight_array[i] = int(input())

print(greedy_rope(weight_array))