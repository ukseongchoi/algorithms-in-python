#더하기 사이클
start_n = input()
start_nn = start_n

if len(start_n) == 1:
    new_n = '0'+start_n
else:
    new_n = start_n

count_ = 0

while True:
    start_n = new_n

    start_len = len(str(start_n)) - 1
    n = start_n
    if len(start_n) == 1:

        n = start_n + '0'

    sum_num = 0
    for i in range(len(n)):

        sum_num = sum_num + int(n[i])

    sum_len = len(str(sum_num)) - 1
    if start_len == 0:
            new_n = '0' +str(sum_num)[sum_len]

    else:
        new_n = start_n[start_len] + str(sum_num)[sum_len]

    count_ = count_ + 1

    if int(start_nn) == int(new_n):
        break

print(count_)
