# https://www.acmicpc.net/problem/1991

from collections import defaultdict

def tree_traversal(tree, root):
    result = [[], [], []]
    def preorder(node):
        if node != '.':
            result[0].append(node)
            preorder(tree[node][0])
            preorder(tree[node][1])
    
    
    def inorder(node):
        if node != '.':
            inorder(tree[node][0])
            result[1].append(node)
            inorder(tree[node][1])
    
    
    def postorder(node):
        if node != '.':
            postorder(tree[node][0])
            postorder(tree[node][1])
            result[2].append(node)
    
    preorder(root)
    inorder(root)
    postorder(root)

    return result

N = int(input())
tree = defaultdict(list)

for n in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

for result in tree_traversal(tree, 'A'):
    print("".join(result))