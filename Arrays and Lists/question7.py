sum = ''
num = (input('Enter a number, enter x to stop: '))

while num != 'x':
    sum+= num + ','
    #num = (input('Enter a number: (press x to stop) '))

values = sum.split(',')[0:-1:1]

#Dictionary
value_count = {}
duped_values = list()

for number in values:

    if number in value_count and duped_values.count(number) == 0:
        duped_values.append(number)
    else:
        value_count.update({number : ''})

print(duped_values)