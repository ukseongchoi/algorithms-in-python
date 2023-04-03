#세막대
a = list(map(int,input().split(' ')))
b = max(a)
c = sum(a)

if c - b <= b:
    k = c - b
    k = k + c - b - 1
    print(k)
else:
    print(c)
