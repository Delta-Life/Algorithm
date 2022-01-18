# https://www.acmicpc.net/problem/2156

def drink(num, scores):
    max_point = [0] * (num+2)
    max_point[1] = scores[1]
    max_point[2] = max_point[1] + scores[2]

    for i in range(3, num+1):
        max_point[i] = max(max_point[i-2] + scores[i], max_point[i-3] + scores[i-1] + scores[i], max_point[i-1])
    
    return max_point[num]

num = int(input())
scores = [0] + [int(input()) for _ in range(num)] + [0]
print(drink(num, scores))