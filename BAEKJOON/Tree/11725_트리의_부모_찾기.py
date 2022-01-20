# https://www.acmicpc.net/problem/11725

import sys
from collections import defaultdict

input = sys.stdin.readline

def get_parent(tree, n):
    parents = []
    parent_dict = {1:0}
    stack = [1]
    while stack:
        node = stack.pop()
        for child in tree[node]:
            if child not in parent_dict:
                stack.append(child)
                parent_dict[child] = node
    for i in range(2, n+1):
        parents.append(parent_dict[i])
    return parents

n = int(input())
tree = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print("\n".join(map(str, get_parent(tree, n))))