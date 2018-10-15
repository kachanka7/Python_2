# ---------------------- CLIENT ----------------------------

import socket, json

from menu import test_send, get_command, print_menu, exit_programm, send_data, menu
from socket_config import get_client_socket

s = get_client_socket()
user_name = input("Введите имя пользователя:    ")
while True:

    print_menu(menu)
    action = int(input("Input command number: \t"))
    command = get_command(menu, action)

    # Такая запись выбора номера команды мне показалась наглядне.
    # К тому же удобно дальнейшее расширение.
    if command == (menu.index("Send_data") + 1):
        text = input("Input text:\t")
        send_data(s, text, user_name)

    elif command == (menu.index("Test_Tx") + 1):
        test_send(s)

    elif command == (menu.index("Exit") + 1):
        exit_programm(s)
        break
