#나머지
list_ = []
for _ in range(10):

    list_.append(int(input()) % 42)

print(len(set(list_)))
