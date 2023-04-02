#삼각형과 세
while True:

    a = list(map(int,input().split(' ')))
    b = max(a)
    c = sum(a)
    d = len(set(a))

    if c == 0 :
        break

    elif c - b <= b:
        print('Invalid')

    elif d == 1:
        print('Equilateral')

    elif d == 2:
        print('Isosceles')

    elif d == 3:
        print('Scalene')
