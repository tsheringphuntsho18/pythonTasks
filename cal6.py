#File handling
#when the file is exists
secret = open('/home/tshering/Desktop/test /secrets.txt', 'r')
print(secret.read())
secret.close()
#when the file does not exist, it gives FileNotFoundError
#to tackle that error
import os
if os.path.isfile("hello.txt"):
    greet = open('/home/tshering/Desktop/test /secrets.txt', 'r')
    print(greet)
    greet.close()
else:
    print("File not found")