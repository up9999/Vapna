import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind('0.0.0.0', '2222')
s.listen(1)
while True:
    conn, adrr = s.accept()
    while True:
        date = conn.recv(1024)
        if not date:
            break
        conn.send('close')
    conn.close()
