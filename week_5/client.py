import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port_num, timeout=None):
        self.host = host
        self.port_num = port_num
        self.timeout = timeout

    def put(self, key, value, timestamp=str(time.time())):
        message = 'put {} {} {}\n'.format(key, value, timestamp)
        with socket.create_connection(self.host, self.port_num) as sock:
            #sock.settimeout(self.timeout)
            sock.send(message.encode())
            answer = sock.recv(1024).decode()
            condition = (answer.split('\n'))[0]
            if(condition == 'error'):
                raise ClientError

    def get(self, key):
        request = 'get {}\n'.format(key)
        with socket.create_connection(self.host, self.port_num) as sock:
            #sock.settimeout(self.timeout)
            sock.sendall(request.encode())

            buffer = sock.recv(1024).decode()
            message = buffer.split('\n')
            condition = message[0]
            if(condition == 'error'):
                raise ClientError
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
                key_val_dict[key] = sorted(key_val_dict[key], key=lambda x: x[1])

            return key_val_dict
