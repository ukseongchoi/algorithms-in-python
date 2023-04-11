#세로읽기
case_list = []
for _ in range(5):
    case_list.append(input())

result = ''

for j in range(15):

    for k in range(5):

        try:
            result = result + case_list[k][j]
        except:
            pass

print(result)
