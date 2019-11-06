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
        if(answer == 'error\nwrong command\n\n'):
            raise ClientError
        return answer

    def put(self, key, value, timestamp=None):
        if not timestamp:
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
        key_val_dict = {}
        for item in tokens:
            splitted_item = item.split()
            key = splitted_item[0]
            value = float(splitted_item[1])
            timestamp = int(splitted_item[2])
            if key not in key_val_dict:
                key_val_dict[key] = (value, timestamp)
            elif type(key_val_dict[key]) == list:
                key_val_dict[key].append((value, timestamp))
            else:
                key_val_dict[key] = [key_val_dict[key], (value, timestamp)]

        #for key in key_val_dict:
         #   key_val_dict[key] = sorted(key_val_dict[key], key=lambda x: x[1])

        return key_val_dict

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    message = 'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
    print(Client.parse_message(message))
