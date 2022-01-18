# https://www.acmicpc.net/problem/13413

def distance(str1, str2):
    return sum([str1[i] != str2[i] for i in range(len(str1))])

def get_diff_num_of_whites(str1, str2):
    return abs(str1.count('W') - str2.count('W'))

def get_min_othello(str1, str2):
    diff = get_diff_num_of_whites(str1, str2)
    return (distance(str1, str2) - diff) // 2 + diff

t = int(input())
for _ in range(t):
    _ = int(input())
    str1 = input()
    str2 = input()
    print(get_min_othello(str1, str2))