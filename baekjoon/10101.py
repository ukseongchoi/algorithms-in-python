#삼각형 외우기
a = int(input())
b = int(input())
c = int(input())

angle_list = [a, b, c]

if sum(angle_list) != 180:
    print('Error')

elif len(set(angle_list)) == 1:
    print('Equilateral')

elif len(set(angle_list)) == 2:
    print('Isosceles')
else:
    print('Scalene')
