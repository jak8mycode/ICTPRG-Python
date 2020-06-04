sum=0
num=(input('Enter a number, enter x to stop: '))
while num !='x':
    sum=sum+int(num)
    num=(input ('Enter a number: (Press x to stop) '))
print('Total '+str(sum))