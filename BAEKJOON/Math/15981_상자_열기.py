#https://www.acmicpc.net/problem/15981

import math

def box_opening(n):
    button_table=[[False] * n for _ in range(int(math.log2(n-1))+1)]
    for j in range(n):
        for x, i in enumerate(str(bin(j))[2:][::-1]):
            if i == '1':
                button_table[x][j] = True
    print(int(math.log2(n-1))+1)
    if n % (2 ** int(math.log2(n-1))) == 1:
        for i in range(int(math.log2(n-1))+1):
            print(n-sum(button_table[i]), " ".join(map(str, [j+1 for j in range(n) if not button_table[i][j]])))
    else:
        for i in range(int(math.log2(n-1))+1):
            print(sum(button_table[i]), " ".join(map(str, [j+1 for j in range(n) if button_table[i][j]])))

n = int(input())
box_opening(n)