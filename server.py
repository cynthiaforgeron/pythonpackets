# Server process

import socket
import sys

def server_process():
    try:
        # Defines a UDP socket and binds to all interfaces
        while True:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_socket.bind(('127.0.0.1', 1234))
            data,address = server_socket.recvfrom(4096)
            data = data.decode("utf-8")
            try:
                float(data)
                new_data = (float(data)) * 2
                if new_data.is_integer():
                    new_data = int(new_data)
                print(new_data)
            except:
                print('Error: input must be a number')
                data,address = server_socket.recvfrom(4096)
            message=str(new_data).encode('utf-8')
            server_socket.sendto(message,address)
            server_socket.close()
    except KeyboardInterrupt:
        sys.exit(0)

    
