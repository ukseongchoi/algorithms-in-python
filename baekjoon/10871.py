#X 보다 작은수

a = list(map(int,input().split()))
b = list(map(int,input().split()))

result = ''
for k in b:
    if k < a[1]:

        result += ' ' + str(k)

print(result[1:])
