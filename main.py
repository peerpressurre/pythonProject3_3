sec = int(input('enter seconds->'))
end = 86400
between = end - sec
h = 0
min = 0

 print (f'Your time: {int(sec/3600)}:{int((sec%3600)/60)}:{int((sec%3600)%60)}')
 if between > 0
  h = int(between/3600)
  min = int((between%3600)/60)
  sec = int((between%3600)%60)
  print (f'Time left: {h}:{min}:{sec}')
 else:
  print('Error!')