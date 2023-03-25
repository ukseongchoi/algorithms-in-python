#오븐시계
a,b = input().split()
c = input()

now_hour = int(a)   #23
now_minute = int(b) #59
run_minute = int(c) #1000

div_minute = divmod((now_minute + run_minute),60)
div_hour = divmod(now_hour + div_minute[0],24)

print(div_hour[1],div_minute[1])
