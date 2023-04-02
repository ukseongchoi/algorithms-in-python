#네번째 점
x_va = []
y_va = []
for _ in range(3):

    a, b =map(int,input().split(' '))

    x_va.append(a)
    y_va.append(b)

print('{} {}'.format(sum(set(x_va))*2 - sum(x_va),sum(set(y_va))*2 - sum(y_va)))
