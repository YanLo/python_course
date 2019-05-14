import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("127.0.0.1", 10001))
    sock.listen(socket.SOMAXCONN)

    conn, addr = sock.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            #process data
            print(data.decode("utf8"))
