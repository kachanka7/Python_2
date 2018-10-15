# ---------------------- SERVER ----------------------------

import socket
import json

s = socket.socket()
s.bind(("localhost", 7777))
print("Server start\n")
s.listen(10)
client, addr = s.accept()

while True:
    print("\nWait data\n")
    data = json.loads(client.recv(2**10).decode("utf-8"))
    if "exit" not in data:
        print("Data receive:\n")
        print(data)

    else:
        client.close()
        print("Client - OUT")
        s.close()
        print("Server - OUT")
        break
