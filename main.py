time = int(input('Enter current time->'))

if 0 < time <6:
    print('Good nigh')
elif time == 6:
    print('Good morning')
elif 6 < time < 13:
    print('Good morning')
elif time == 13:
    print('Good day')
elif 13 < time < 17:
    print('Good day')
elif time == 17:
    print('Good evening')
elif 17 < time < 24:
    print('Good evening')
elif time == 24:
    print('Good evening')
else:
    print('Error')