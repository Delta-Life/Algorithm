# https://www.acmicpc.net/problem/1655

import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_heap, min_heap = [], []

for i in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if len(min_heap) >= 1 and max_heap[0] * -1 > min_heap[0]:
        max_value = heapq.heappop(max_heap) * -1
        min_value = heapq.heappop(min_heap)
        
        heapq.heappush(max_heap, min_value * -1)
        heapq.heappush(min_heap, max_value)

    print(max_heap[0] * -1)