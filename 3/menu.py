import socket
import json
import os

menu = ["Send_data", "Test_Tx", "Exit"]


def print_menu(menu):
    for i, k in enumerate(menu, start=1):
        print(f'{i}.{k}')


def get_command(menu):
    while True:
        command = int(input("Input comand number: \t"))
        if 1 <= command <= len(menu):
            return command
        else:
            print("Error command input. Try again.")


def exit_programm(s):
    s.send(json.dumps({"exit":"exit"}).encode("utf-8"))
    print("EXIT")
    exit()


def test_send(s):

    test_message = {
        "TEST": "SEND",
        "Dir": os.getcwd()
    }
    s.send(json.dumps(test_message).encode("utf-8"))
    print("\n------------test end--------------\n")

# if __name__ == '__main__':
