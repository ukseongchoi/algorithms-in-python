#A+B - 7
T = int(input())

for count in range(1,T+1):

    a, b = input().split()
    print('Case #'+ str(count)+': '+str(int(a)+int(b)))
