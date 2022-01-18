# https://www.acmicpc.net/problem/1912

def max_sum_subsequence(num_array):
    max_array = [0] * len(num_array)
    max_array[0] = num_array[0]

    for i in range(1, len(num_array)):
        max_array[i] = max(num_array[i], num_array[i] + max_array[i-1])
    
    return max(max_array)

n = int(input())
num_array = list(map(int, input().split()))

print(max_sum_subsequence(num_array))