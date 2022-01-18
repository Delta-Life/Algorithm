# https://www.acmicpc.net/problem/13164

def get_min_cost(height_array, k):
    height_array.sort()
    for i in range(len(height_array)-1, 0, -1):
        height_array[i] -= height_array[i-1]
    
    height_array.pop(0)
    height_array.sort()
    for i in range(k-1):
        height_array.pop()
    
    return sum(height_array)

n, k = map(int, input().split())
height_array = list(map(int, input().split()))

print(get_min_cost(height_array, k))