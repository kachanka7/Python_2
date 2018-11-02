import socket, json, os, datetime

menu = ["Send_data", "Test_Tx", "Exit"]
now_time = datetime.datetime.now()



def print_menu(menu):
    for i, k in enumerate(menu, start=1):
        print(f'{i}.{k}')


def get_command(menu, command):
    while True:
        # command = int(input("Input command number: \t"))
        if 1 <= command <= len(menu):
            return command
        else:
            print("Error command input. Try again.")


def send_data(s, text, user_name='User'):
    data_tx = {
        "text": text,
        "user_name": user_name
    }
    s.send(json.dumps(data_tx).encode("utf-8"))
    print("Data send\n")


def exit_programm(s):
    s.send(json.dumps({"exit": "exit"}).encode("utf-8"))
    print("EXIT")
    exit()


def test_send(s):
    test_message = {
        "text": "SEND TEST MESSAGE",
        "dir": os.getcwd(),
        "user_name": "USER",
        "time": [now_time.hour, now_time.minute, ]
    }
    s.send(json.dumps(test_message).encode("utf-8"))
    print("\n------------test end--------------\n")


# if __name__ == '__main__':