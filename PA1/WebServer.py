# Full Name: Dylan Ravel
# Student ID: 2445987
# Chapman Email: ravel@chapman.edu
# Course Number and Section: CPSC-353-03
# Assignment: Prog-Assign -1 : Web Server Note


from socket import *
import sys

HOST = ""
PORT = 6789
BUFFER_SIZE = 1024

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    try:
        message = connectionSocket.recv(BUFFER_SIZE).decode()
        filename = message.split()[1]

        with open(filename[1:]) as file:
            outputData = file.read()

        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(outputData.encode())

    except IOError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response += "<h1>404 Not Found</h1><p>The requested file could not be found.</p>"
        connectionSocket.send(response.encode())

    finally:
        connectionSocket.close()

serverSocket.close()
sys.exit()