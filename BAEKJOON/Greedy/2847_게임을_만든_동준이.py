# https://www.acmicpc.net/problem/2847

def greedy_score(score_array):
    before_score = score_array[-1]
    count = 0
    for score in score_array[::-1][1:]:
        if score >= before_score:
            count += score - before_score + 1
            before_score -= 1
        else:
            before_score = score
    return count


N = int(input())
score_array = [0] * N

for i in range(N):
    score_array[i] = int(input())

print(greedy_score(score_array))