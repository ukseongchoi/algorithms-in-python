#별찍 7
#입력
n = int(input())

#길이 만들기
zero_len = ''
for k in range(n):
    zero_len = zero_len + ' '

#왼쪽부터 별을 찍고 반전 시키기
star_list = []
for k in range(n):
    g = zero_len.replace(' ', '*' ,k+1)

    star_list.append(g[::-1])

# N번째 Star_list 에서 N-1번 별을 추가하여 리스트에 저장
for k in range(n):
    if k > 0:
        star_num = ''
        for _ in range(k):
            star_num = star_num + '*'

        star_list[k] = star_list[k] + star_num

# 2N - 1 번까지 그리기 위해 X축 대칭
r_star_list = list(reversed(star_list))

#같은항목 삭제
del r_star_list[0]

#이어 붙이기
result = star_list + r_star_list

#결과
for k in result:
    print(k)
