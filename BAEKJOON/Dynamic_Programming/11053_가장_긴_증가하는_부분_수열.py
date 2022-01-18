# https://www.acmicpc.net/problem/11053

def LIS(num_array):
    lis_array = [1] * len(num_array)

    for i in range(len(num_array)):
        for j in range(i):
            if num_array[i] > num_array[j]:
                lis_array[i] = max(lis_array[i], lis_array[j]+1)
    
    return max(lis_array)

_ = int(input())
num_array = list(map(int, input().split()))

print(LIS(num_array))