import socket
import select
import sys
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])"""

IP_address = socket.gethostname()
Port = 5555

server.connect((IP_address, Port))

# asks for user name
name = "Periodic Client"
server.sendall(name.encode())

loop = True
while loop:

    message = "*** ATTENTION: Message from Periodic Client ***"
    server.sendall(message.encode())

    time.sleep(30)

server.close()
