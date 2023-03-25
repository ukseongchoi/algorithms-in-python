#A+B - 8
T = int(input())

for count in range(1,T+1):

    a, b = input().split()
    print('Case #'+ str(count)+': '+a+' + '+b+' = '+str(int(a)+int(b)))
