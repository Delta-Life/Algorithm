#https://www.acmicpc.net/problem/1463

def min_calculation(num):
    min_array = [0] * (num+1)
    for i in range(2, num+1):
        min_array[i] = min_array[i-1] + 1
        if i % 3 == 0:
            min_array[i] = min(min_array[i], min_array[i//3]+1)
        if i % 2 == 0:
            min_array[i] = min(min_array[i], min_array[i//2]+1)
    
    return min_array[-1]

x = int(input())

print(min_calculation(x))