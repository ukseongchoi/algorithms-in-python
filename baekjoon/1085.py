#직사각형에서 탈출
import math
a = list(map(int,input().split(' ')))
d_x = abs(a[0]-a[2])
d_y = abs(a[1]-a[3])
print(min([a[0],a[1],d_x,d_y]))
