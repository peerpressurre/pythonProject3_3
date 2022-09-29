p = int(input('enter price->'))
q = int(input('enter quantity->'))
d = int(input('enter discount->'))

print ('| sum -> summary\n| pwd -> price of one console considering discount')

op = input('->')
res = ''
sum1 = (int(p*q))

if op == 'sum':
    res = int(sum1-((d*sum1)/100))
elif op == 'pwd':
    res = int(p-((d*p)/100))

    print(f'res = {res}')

