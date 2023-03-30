#단어공부
wold = input()
wold_s = wold.lower()

dic_w = {}
for k in set(list(wold_s)):
    dic_w[k] = wold_s.count(k)

max_num = max(sorted(dic_w.values(), reverse=True))

result = []
for key, value in dic_w.items():
    if value == max(sorted(dic_w.values(), reverse=True)):
        result.append(key)

if len(result) >= 2:
    print('?')
else:
    print(result[0].upper())
