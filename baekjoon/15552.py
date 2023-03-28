#빠른 A+B
import sys
T = int(input())

for _ in range(T):

    a = sys.stdin.readline().strip().split(' ')
    print(int(a[0])+int(a[1]))
