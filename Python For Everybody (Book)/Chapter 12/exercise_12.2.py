# Python For Everybody Chapter 12 Exercise 2

# Change the socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of characters and display the count of the number os characters at the end of the document.

import socket

web = input('Enter a website: ')
host = web.split('/')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host[2], 80))
cmd = 'GET ' + web + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)


count = 0

while count < 3000:
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    count += len(data)
    print(data.decode(), end="")
    print(count)
mysock.close()

