var1 = input('type a number: ')
var2 = input('type another number: ')
var3 = (int(var1) + (int(var2)))

myFile = open('maths.txt', 'w')
myFile.write(str(var3))
myFile.close()