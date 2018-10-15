import unittest, json, socket, threading
from menu import menu, get_command, send_data


def client_connect():
    s = socket.socket()
    s.connect(('localhost', 7777))

    send_data(s, 'test_data')


class TestClass(unittest.TestCase):

    def test_get_command(self):
        men_u = ['First', 'second', 'third', ]
        self.assertEqual(get_command(men_u, len(men_u) - 1), len(men_u) - 1,
                         "Incorrectly command number!")

    # Тест функции отправки сообщения.
    def test_send_data(self):
        t = threading.Thread(target=client_connect, daemon=True)

        t.start()

        s = socket.socket()
        s.bind(('localhost', 7777))
        s.listen(10)
        s.settimeout(5)

        try:
            client, addr = s.accept()
            data = json.loads(client.recv(2 ** 10).decode('utf-8'))
            data_rx = data["text"]
            self.assertEqual(data_rx, "test_data", "Data incorrect!")

            client.close()
            s.close()
        except socket.timeout:
            self.fail("Accept failed")


if __name__ == "__main__":
    unittest.main()
