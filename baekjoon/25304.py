#영수증
a = int(input())
b = int(input())

result = 0
for _ in range(b):
    c,d = map(int, input().split())
    result += c * d

if a == result:
    print('Yes')

else:
    print('No')
