d = int(input('enter diameter->'))

print ('| per -> perimetr\n| a-> area')
op = input('->')
res = ''
if op == 'per':
    res = int(2*3.14*(d/2))
elif op == 'a':
    res = int((3.14*d**2/4))

    print(f'res = {res}')

