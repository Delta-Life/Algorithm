#https://www.acmicpc.net/problem/9465

def get_max_score(score_matrices):
    result = []
    for score_matrix in score_matrices:
        if len(score_matrix[0]) > 1:
            score_matrix[0][1] += score_matrix[1][0]
            score_matrix[1][1] += score_matrix[0][0]
        for i in range(2, len(score_matrix[0])):
            score_matrix[0][i] += max(score_matrix[1][i - 1], score_matrix[1][i - 2])
            score_matrix[1][i] += max(score_matrix[0][i - 1], score_matrix[0][i - 2])
        result.append(max(score_matrix[0][-1], score_matrix[1][-1]))
    
    return result


T = int(input().rstrip())
score_matrices = []

for i in range(T):
    _ = input()
    score_matrices.append([list(map(int, input().split())), list(map(int, input().split()))])

print("\n".join(map(str, get_max_score(score_matrices))))