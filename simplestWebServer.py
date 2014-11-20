# cdoing=utf-8

import socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(('', 80))  # remember, 80 is the port for HTTP traffic
listen_socket.listen(1)
connection, adress = listen_socket.accept()
while True:
    connection.recv(1024)
    connection.sendall("""HTTP/1.1 200 OK
    Content-type: text/html


    <html>
        <body>
            <h1>Hello, World!</h1>
        <body>
    </html>""")
    connection.close()