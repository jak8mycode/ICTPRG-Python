username = input("Enter a username: ")
password = input("Enter a password: ")

myFile = open('logins.txt', 'r')
contents = myFile.read()
lines = contents.split('\n')
for line in lines:
    if len(line.split(':')) !=2:
        continue
    user = line.split(':')[0]
    pswd = line.split(':')[1]

    if user == username and pswd == password:
        print('username?: ' + user + ' password?: ' + password + ' Access Granted!')
    
myFile.close()