#색종이
n = int(input())

info_n = []
for _ in range(n):
    info_n.append(list(map(int,input().split(' '))))

one_vetor = [1,1,1,1,1,1,1,1,1,1]

matrix = []
for _ in range(101):

    vetor = []
    for _ in range(101):
        vetor.append(0)

    matrix.append(vetor)

for j in range(n):

    for k in range(10):

        matrix[info_n[j][0]:info_n[j][0]+10][k][info_n[j][1]:info_n[j][1]+10] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


S = 0
for k in range(101):
    S = S + sum(matrix[k])

print(S)
