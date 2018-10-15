import socket
import json
from menu import test_send, get_command, print_menu, exit_programm

menu = ["Send_data", "Test_Tx", "Exit"]
s = socket.socket()
s.connect(("localhost", 7777))


while True:
    print_menu(menu)
    command = get_command(menu)

    if command == 1:

        data_tx = {
            "text": input("Input text:\t")
        }
        s.send(json.dumps(data_tx).encode("utf-8"))
        print("Data send")

    elif command == 2:
        test_send(s)

    elif command == 3:
        exit_programm(s)
        break
