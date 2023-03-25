#구구단
a = input()
n = int(a)
nums = [1,2,3,4,5,6,7,8,9]
for k in nums:
    c = str(n*k)

    print(str(n) +' * '+ str(k)+' = ' + c)
