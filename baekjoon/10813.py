#공 바꾸기
N, M = map(int, input().split())

basket = []
for k in range(N):
    basket.append(k+1)

for _ in range(M):
    c_n_1,c_n_2 = map(int,input().split(' '))

    change_to_1 = basket[c_n_1-1]
    change_to_2 = basket[c_n_2-1]

    basket[c_n_1-1] = change_to_2
    basket[c_n_2-1] = change_to_1

result = ''
for k in basket:
    result +=  ' '+ str(k)

print(result[1:])
