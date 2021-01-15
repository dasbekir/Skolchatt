import socket
import threading
import pymysql
from dbFunctions import DbFunctions


def onNewClient(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"New Connection was made from ({ip}, {port})")

    name = client.recv(1024)
    name = name.decode()

    if name == "Periodic Client":
        print("")
    else:
        mssg = name + " Joined the Chat."
        sendToAll(client, mssg)
        db.addNewCol(name)

    while True:
        msg = client.recv(1024)

        if msg:
            if msg.decode().upper() == "QUIT":
                print(name + " Disconnected...")
                msg = name + " Left the Chat."
                sendToAll(client, msg)
                remove(client)
                break
            else:
                if name == "Periodic Client":
                    print("")
                else:
                    db.insertMessage(name, msg.decode())
                    msg = "(" + name + "): " + msg.decode()
                # print(msg)
                sendToAll(client, msg)

        else:
            remove(client)


def sendToAll(client, message):
    # Message not forwarded to server and sender itself
    for sock in connectionsList:
        if sock != server_sock and client != sock:
            try:
                sock.sendall(message.encode())
            except Exception as e:
                # if connection not available
                print(e)
                sock.close()
                remove(sock)


def remove(sock):
    if sock in connectionsList:
        connectionsList.remove(sock)


# ----------- MAIN -----------------------

server_sock = socket.socket()
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#IP = socket.gethostname()
IP = "127.0.0.1"
port = 5555

connectionsList = []
clientsRecords = {}

db = DbFunctions()
db.connectDb()
db.createTables()

try:
    server_sock.bind((IP, port))
    server_sock.listen(10)
    print("Server Listening....")
except Exception as e:
    print(e)

while True:
    try:
        clientfd, addr = server_sock.accept()
        threading._start_new_thread(onNewClient, (clientfd, addr))
        connectionsList.append(clientfd)

    except Exception as e:
        print(e)

server_sock.close()
