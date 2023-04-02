#대지
n = int(input())
x_va = []
y_va = []
for _ in range(n):

    a, b =map(int,input().split(' '))

    x_va.append(a)
    y_va.append(b)

dx = max(x_va) - min(x_va)
dy = max(y_va) - min(y_va)

print(dx * dy)
