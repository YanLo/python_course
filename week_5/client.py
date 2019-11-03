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
        with socket.create_connection(self.host, self.port_num) as sock:
            message = 'put {} {} {}\n'.format(key, value, timestamp)
            sock.sendall(message)
            answer = sock.recv(1024)
            str_ans = answer.decode()
            condition = (str_ans.split('\n'))[0]
            if(condition == 'error'):
                raise ClientError

    def get(self, key):
        with socket.create_connection(self.host, self.port_num) as sock:
            message = 'get {}\n'.format(key)
            sock.sendall(message)

            all_data = []
            while True:
                data = sock.recv(1024)
                all_data.append(data)
                if not data:
                    break

            buffer = all_data.decode()
            message = buffer.split('\n')
            condition = message[0]
            if(condition == 'error'):
                raise ClientError
            info_messages = message[1:-2]
            key_val_dict = {}
            for item in info_messages:
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
                key_val_dict[key] = sorted(key_val_dict[key], key=lambda x: x[0])

            return key_val_dict
