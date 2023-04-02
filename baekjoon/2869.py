#달팽이는 올라가고싶다.
import math
a = list(map(int,input().split(' ')))

power = a[2] - a[0]
up_power = a[0] - a[1]

if power == 0:
    print('1')

else:
    print(math.ceil(power / up_power)+1)
