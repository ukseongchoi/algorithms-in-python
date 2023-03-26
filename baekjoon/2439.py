#별찍기2
n = int(input())
len_n = ''
for k in range(n):
    len_n = len_n + ' '

for k in range(n):
    g = len_n.replace(' ', '*' ,k+1)
    print(g[::-1])
