#1 Гігабайт = 8589934592 Біт
size = int(input('enter file size->'))
speed = int(input('enter connection speed->'))

print('| h -> hours\n| min -> minutes\n| sec -> seconds')
op = input('->')
res = ''
bsize = int(size*8589934592)

if op == 'h':
    res = int((bsize/speed)/3600)
elif op == 'min':
    res = int((bsize/speed)/60)
elif op == 'sec':
    res = int(bsize/speed)

print(f'res = {res}')


