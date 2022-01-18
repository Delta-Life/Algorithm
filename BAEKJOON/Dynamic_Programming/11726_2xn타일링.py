# https://www.acmicpc.net/problem/11726

def get_num_of_case(num):
    min_array = [1, 2]
    for i in range(2, num):
        min_array.append((min_array[i-1] + min_array[i-2]) % 10007)
    return min_array[num-1]

n = int(input())
print(get_num_of_case(n))