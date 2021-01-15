import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, PORT number")
    exit()
IP = str(sys.argv[1])
PORT = int(sys.argv[2])

#IP = socket.gethostname()
#PORT = 5555

server.connect((IP, PORT))

# asks for user name
name = input("CREATING NEW ACCOUNT:\n Enter username:")
server.sendall(name.encode())
print("\nYou have joind the Chat room. Enter 'quit' any time to leave.\n")

loop = True
while loop:
    sockList = [sys.stdin, server]
    readSocks, writeSocks, errSocks = select.select(
        sockList, [], [])
    for socks in readSocks:
        if socks == server:
            message = socks.recv(1024)
            message = message.decode()
            print(message)
        else:
            message = input()
            server.send(message.encode())
            print(f"(You): {message}")

            if message.upper() == "QUIT":
                print("\n...You Left the Chat...\n")
                loop = False
                break

server.close()
