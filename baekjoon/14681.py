#사분면 고르기
a = input()
b = input()

x = int(a)
y = int(b)

if x >= 0 and y>=0:
    print(1)

elif x <=0 and y>=0:
    print(2)

elif x >=0 and y <= 0:
    print(4)

elif x <=0 and y <= 0:
    print(3)
