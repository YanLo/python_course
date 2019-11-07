import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port_num, timeout=None):
        self.socket = socket.create_connection((host, port_num), timeout)

    def send_and_recieve(self, request):
        socket = self.socket
        socket.sendall(request)
        answer = socket.recv(1024).decode()
        if answer == 'error\nwrong command\n\n':
            raise ClientError
        return answer

    def put(self, key, value, timestamp=None):
        if timestamp == None:
            timestamp = str(int(time.time()))
        message = 'put {} {} {}\n'.format(key, value, timestamp)
        self.send_and_recieve(message)

    def get(self, key):
        request = 'get {}\n'.format(key)
        respond = self.send_and_recieve(request)
        return self.parse_message(respond)

    @staticmethod
    def parse_message(buff):
        message = buff.split('\n')
        tokens = message[1:-2]
        key_val_list = []
        for item in tokens:
            splitted_item = item.split()
            key = splitted_item[0]
            value = float(splitted_item[1])
            timestamp = int(splitted_item[2])
            key_val_list.append((key, value, timestamp))
            sorted_list = sorted(key_val_list, key=lambda x: x[2])

        key_val_dict = dict()
        for key, value, timestamp in key_val_list:
            key_val_dict.setdefault(key, []).append((timestamp, value))

        return key_val_dict

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    message = 'ok\npalm.cpu 10.5 1501864247\npalm.cpu 10.6 1600000000\neardrum.cpu 15.3 1501864259\n\n'
    print(Client.parse_message(message))
