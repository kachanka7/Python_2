# ---------------------- SERVER ----------------------------

import socket
import json
from socket_config import get_server_socket

s = get_server_socket()
print("Server start")
client, addr = s.accept()


while True:
    print("\nWait data\n")
    data = json.loads(client.recv(2 ** 10).decode("utf-8"))

    if "exit" not in data:
        if "Connect" in data:
            print(f"User:\t{data['user_name']['account_name']}\n"
                  f"Status:\t{data['user_name']['status']}")
        else:
            print("Data receive:")
            print(f'{data["user_name"]}:\t{data["text"]}')
        if "dir" in data:
            print(f"Current dir:\t{data['dir']}")
            print(f"Current time:\t{str(data['time'][0]) + ':' + str(data['time'][1])}")

    else:
        client.close()
        print("Client - OUT")
        s.close()
        print("Server - OUT")
        break
