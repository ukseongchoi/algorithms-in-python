#윤년
a = input()
A = int(a)

if A%4 == 0:

    if A%100 == 0:

        if A%400 == 0:
            print('1')

        else:
            print('0')

    else:
        print('1')

else:
    print('0')
