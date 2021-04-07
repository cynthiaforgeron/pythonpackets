# Server process

import socket
import sys

def server_process():
    try:
        # Defines a UDP socket and binds to all interfaces
        while True:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_socket.bind(('0.0.0.0', 1234))
            data,address = server_socket.recvfrom(4096)
            data = data.decode("utf-8")
            # Checks if message received can be converted to float
            # If so, it checks to see that it is an integer, converts to integer to avoid ".0" outputs,
            # then multiples the number * 2 and sends it back to the client, then closes the socket 
            # If not, it prints an error, and sends the message back to the client, then closes the socket
            try:
                float(data)
                new_data = (float(data)) * 2
                if new_data.is_integer():
                    new_data = int(new_data)
                print(new_data)
                message=str(new_data).encode('utf-8')
                server_socket.sendto(message,address)
                server_socket.close()
            except:
                new_data = data
                print('Error: input must be a number')
                message=str(data).encode('utf-8')
                server_socket.sendto(message,address)
                server_socket.close()
    # This silences traceback on ctrl-break or ctrl-c
    except KeyboardInterrupt:
        sys.exit(0)
