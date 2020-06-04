sum = ''
num = (input('Enter a number, enter x to stop: '))
while num != 'x':
    sum += num + ','
    num = (input('Enter a number: (Press x to stop) '))

print('Values: ', sum.split(',')[0:-1:1])