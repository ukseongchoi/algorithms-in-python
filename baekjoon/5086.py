#약수와 배수

def magic(numbers):

    if numbers[0] % numbers[1] == 0:
        print('multiple')

    elif numbers[1] % numbers[0] == 0:
        print('factor')

    else:
         print('neither')

while True:
    n = list(map(int,input().split(' ')))

    if [0, 0] == n:
        break

    else:
        magic(n)
