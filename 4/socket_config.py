import socket, json, random, datetime
# import menu

ADRESS = "localhost"
PORT = 7777
now_time = datetime.datetime.now()


def get_client_socket():
    s = socket.socket()
    s.connect((ADRESS, PORT))

    data_connect_send = {
        "Connect": "presence",
        "time": [now_time.hour, now_time.minute, ],
        "type": "status",
        "user_name": {
            "account_name": f"User#{random.randint(1, 100)}",
            "status": "Connect done"
        }
    }
    s.send(json.dumps(data_connect_send).encode("utf-8"))
    return s


def get_server_socket():
    s = socket.socket()
    s.bind((ADRESS, PORT))
    s.listen(10)
    return s
