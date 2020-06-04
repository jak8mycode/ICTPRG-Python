myFile = open('names.txt', 'r')
contents = myFile.read()
print(contents)
myFile.close()

myFile = open('names-formated.txt', 'w')
myFile.write(contents.title())
myFile.close()