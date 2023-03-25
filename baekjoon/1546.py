#평균
a = int(input())
b = list(map(int,input().split()))

point_max= max(b)
new_sum = 0
for k in b:
    new_sum += k/point_max*100

print(new_sum/a)
