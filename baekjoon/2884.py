#알람 시계
a,b = input().split()

hour = int(a)
minute = int(b)

minute_result = minute - 45

if hour > 0:

    if minute_result >= 0:
        print(hour, minute_result)

    else:
        print(hour-1,60+minute_result)

else:

    if minute_result >= 0:
        print(hour, minute_result)

    else:
        print(23,60+minute_result)
