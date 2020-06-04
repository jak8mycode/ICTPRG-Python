# myFile is the pointer file
#open func opens a file
# 1st argument = name of the file
# 2nd argument = how it should be opened
myFile = open('guestlist.txt', 'r')

#contents = myFile.read()

line = myFile.readline()

while (line != ''):
#hidden character within (line)
    print(line.strip())
    line = myFile.readline()