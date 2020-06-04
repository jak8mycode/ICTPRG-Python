number = input('Enter a large number: ')
sum = 0
sum_str = ''

for character in number:
    sum += int(character)
    sum_str += character + ' + '

print(sum_str[0:-2:1] + ' = ' + str(sum))