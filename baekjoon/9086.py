#문자열
case_N = int(input())
for _ in range(case_N):
    result_str = input()
    print('{}{}'.format(result_str[0],result_str[-1]))
