name = input('Enter First Name: ')
names = name.split(' ')
initals = ''

for val in names:
    initals += val[0]
    
print(initals)