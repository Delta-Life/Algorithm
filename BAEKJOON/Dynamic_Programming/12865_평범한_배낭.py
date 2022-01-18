# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

num, max_weight = map(int, input().split())
weight_list, value_list = [], []
tmp_table = [[0]*(max_weight+1) for _ in range(num+1)]

for _ in range(num):
    a, b = map(int, input().split())
    weight_list.append(a)
    value_list.append(b)

for i in range(1, num+1):
    for j in range(1, max_weight+1):
        if j < weight_list[i-1]:
            tmp_table[i][j] = tmp_table[i-1][j]
        else:
            tmp_table[i][j] = max(tmp_table[i-1][j], tmp_table[i-1][j-weight_list[i-1]] + value_list[i-1])

print(tmp_table[num][max_weight])