sum=""
num=(input('Enter a Name, hit enter on a blank space to stop" '))
while num !='':
    sum=sum+str(num) + '\n'
    num=(input ('Enter another name, hit enter on a blank space to stop: '))
    
#print(sum)
myFile = open('people.txt', 'w')
myFile.write(sum)
myFile.close()