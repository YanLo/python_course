import socket
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(host, port_num, timeout=None):
        self.host = host
        self.port_num = port_num
        self.timeout = timeout

    def put(metric_name, metric_val, timestamp):
        try:
            with socket.create_connection(self.host, self.port_num) as sock:
                if (timestamp == None):
                    sock.sendall((metric_name, metric_val, str(time.time)))
                else:
                    sock.sendall((metric_name, metric_val, timestamp))
        except ClientError:
            pass

    def get(metric_name):
        try:
            with socket.create_connection(self.host, self.port_num) as sock:
                #send metric_name for getting an answer
                sock.sendall(metric_name)

                #now we actually get an answer
                sock.bind((self.host, self.port_num))
                sock.listen()
                conn, addr = sock.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(data.decode("utf8"))

        except ClientError:
            pass
