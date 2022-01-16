#https://www.acmicpc.net/problem/2579

def walk_up(num, stairs):
    max_point = [0] * (num+2)
    max_point[1] = stairs[1]
    max_point[2] = max_point[1] + stairs[2]

    for i in range(3, num+1):
        max_point[i] = max(max_point[i-2], max_point[i-3] + stairs[i-1]) + stairs[i]
    
    return max_point[num]

num = int(input())
stairs = [0] + [int(input()) for _ in range(num)] + [0]
print(walk_up(num, stairs))