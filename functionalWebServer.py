# coding=utf-8

"""A web server capable of serving files from a given directory."""

import sys
import socket
import os.path 

DOCUMENT_ROOT = '/home/solo'
RESPONSE_TEMPLATE = """HTTP/1.1 200 OK
Content-Length: {}

{}"""

def main():
    """Main entry point for script"""
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('', int(sys.argv[1])))
    listen_socket.listen(1)

    while True:
        connection, adress = listen_socket.accept()
        request = connection.recv(1024)
        start_line = request.split('\n')[0]
        method, uri, version = start_line.split()
        path = DOCUMENT_ROOT + uri
        print(path)
        if not os.path.exists(path):
            connection.sendall('HTTP/1.1 404 Not Found\n')
        else:
            with open(path) as file_handle:
                file_contents = file_handle.read()
                response = RESPONSE_TEMPLATE.format(
                    len(file_contents), file_contents)
                connection.sendall(response)
        connection.close()

if __name__ == '__main__':
    sys.exit(main()) 

"""
To run this and see something in your browser, 
open a Terminal session (or whatever the equivalent is on Windows) and navigate to the directory you saved this file in. 
Once there, create a text file named hello.txt with with "hello" as the contents. 
Save it in the /tmp (or another directory of your choosing). 
Run the script by typing python <name_of_file.py> 8080 /tmp. 
Open your browser and navigate to http://localhost:8080/hello.txt. 
"""