# myFile is the pointer file
#open func opens a file
# 1st argument = name of the file
# 2nd argument = how it should be opened
myFile = open('guestlist.txt', 'r')

for line in myFile:
    print(line.strip())

myFile.close()

# 'a' will add / appened. 'w' will overwrite
myFile = open('guestList.txt', 'a')
myFile.write('Joe\n')
myFile.close()

myFile = open('guestList.txt', 'r')

for line in myFile:
    print(line.strip())

myFile.close()