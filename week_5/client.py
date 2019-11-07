import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port_num, timeout=None):
        self.socket = socket.create_connection((host, port_num), timeout)

    def send_and_recieve(self, request):
        socket = self.socket
        socket.sendall(request.encode())
        answer = socket.recv(4096).decode()
        if answer == 'error\nwrong command\n\n':
            raise ClientError
        return answer

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        message = 'put {} {} {}\n'.format(key, value, timestamp)
        self.send_and_recieve(message)

    def get(self, key=None):
        request = 'get {}\n'.format(key)
        respond = self.send_and_recieve(request)
        return self.parse_message(respond)

    @staticmethod
    def parse_message(buff):
        message = buff.split('\n')
        tokens = message[1:-2]
        key_val_list = []
        for item in tokens:
            key, value, timestamp = item.split()
            key_val_list.append((key, float(value), int(timestamp)))
            sorted_list = sorted(key_val_list, key=lambda x: x[2])

        key_val_dict = dict()
        for key, value, timestamp in key_val_list:
            key_val_dict.setdefault(key, []).append((timestamp, value))

        return key_val_dict

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    message = 'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
    print(Client.parse_message(message))
