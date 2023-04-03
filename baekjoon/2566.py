#최댓값
matrix = []
x_line = [0,0,0,0,0,0,0,0,0,0]
matrix.append(x_line)
for _ in range(9):
    vetor_ = list(map(int,input().split(' ')))
    matrix.append([0]+vetor_)

max_y_vector = []
for k in range(10):
    vetor_max_value = max(matrix[k])
    vetor_max_index = matrix[k].index(vetor_max_value)
    max_y_vector.append([vetor_max_value,vetor_max_index])

max_x_vector = []
for k in range(10):
    max_x_vector.append(max_y_vector[k][0])

max_x_index = max_x_vector.index(max(max_x_vector))
max_y_index = max_y_vector[max_x_vector.index(max(max_x_vector))][1]
if max_x_index + max_y_index == 0:
    max_x_index = 1
    max_y_index = 1

print(max(max_x_vector))
print(max_x_index,max_y_index)
