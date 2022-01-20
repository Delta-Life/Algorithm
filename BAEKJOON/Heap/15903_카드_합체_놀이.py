# https://www.acmicpc.net/problem/15903

import heapq

def get_card_game(cards, m):
    heap = []

    for i in range(n):
      heapq.heappush(heap, cards[i])
    
    for i in range(m):
      x = heapq.heappop(heap)
      y = heapq.heappop(heap)
      heapq.heappush(heap, x+y)
      heapq.heappush(heap, x+y)
    return sum(heap)

n, m = map(int, input().split())
cards = list(map(int, input().split()))
 
print(get_card_game(cards, m))