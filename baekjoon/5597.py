#과제 안내신분

def find_N(n_list, number):

    a = None
    for list_n in n_list:

        if list_n == number:
            a = True

    if a == True:
        return True

    else:
        return False

stu_N = []
for k in range(30):
    stu_N.append(k+1)

numbers = []
for _ in range(28):

    numbers.append(int(input()))

for j in stu_N:

    if find_N(numbers, j) == False:
        print(j)
