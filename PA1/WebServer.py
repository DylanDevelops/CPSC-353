# Full Name: Dylan Ravel, Kyla Cabrera, and Noslen Cruz-Muniz
# Student ID: 2445987, 2445213, 2447745
# Chapman Email: ravel@chapman.edu, kycabrera@chapman.edu, and cruzmuniz@chapman.edu
# Course Number and Section: CPSC-353-03
# Assignment: Programming Assignment 1

from socket import *
import sys

HOST = ""
PORT = 6789
BUFFER_SIZE = 1024

# creates the socket to attach to
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    try:
        # try to get the file requested
        message = connectionSocket.recv(BUFFER_SIZE).decode()
        filename = message.split()[1]

        with open(filename[1:]) as file:
            outputData = file.read()

        # if found, return the file
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(outputData.encode())

    except IOError:
        # if there is an error, tell the user it is a 404 error
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response += "<h1>404 Not Found</h1><p>The requested file could not be found.</p>"
        connectionSocket.send(response.encode())

    finally:
        # close out the connection when done
        connectionSocket.close()

serverSocket.close()
sys.exit()