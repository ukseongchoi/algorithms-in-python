#주사위 세개
a, b, c = input().split()

noon_list = [a, b, c]
noon_set = (set(noon_list))
noon_max = int(max(noon_set),)
noon_count_max = int(max(noon_list, key = noon_list.count))

if len(noon_set) == 1:
    print(10000+noon_max*1000)

elif len(noon_set) == 3:
    print(noon_max*100)

else:
    print(1000+noon_count_max*100)
