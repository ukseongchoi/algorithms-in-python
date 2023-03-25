#나머지
a, b, c = input().split()

A = int(a)
B = int(b)
C = int(c)

print((A+B)%C,((A%C)+(B%C))%C,(A*B)%C,((A%C) * (B%C))%C, sep = '\n')
