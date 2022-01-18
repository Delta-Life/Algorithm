# https://www.acmicpc.net/problem/1449

def greedy_min_tape(index_array, L):
    index_array.sort()
    count = 0
    dst = 0
    
    for i in index_array:
        if i > dst:
            count += 1
            dst = i + L - 1
    
    return count

_, L = map(int, input().split())
index_array = list(map(int, input().split()))

print(greedy_min_tape(index_array, L))