#행렬덧셈
case_N = list(map(int,input().split(' ')))

matrix_A = []
for _ in range(case_N[0]):
    matrix_A.append(list(map(int,input().split(' '))))

matrix_B = []
for _ in range(case_N[0]):
    matrix_B.append(list(map(int,input().split(' '))))

matrix_A_B = []
for j in range(case_N[0]):
    vector = []
    for k in range(case_N[1]):

        vector += [matrix_A[j][k] + matrix_B[j][k]]

    matrix_A_B += [vector]

for k in range(case_N[0]):
    print(str(matrix_A_B[k]).replace('[','').replace(']','').replace(',',''))
