# Client process

import socket
import sys

def client_process(msg, ip_destination):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(msg.encode("utf-8"),(ip_destination, 1234))
        client_socket.settimeout(5)
        data,address=client_socket.recvfrom(4096)
        print("Server at " + str(address[0]) + ", " + str(address[1]) + " replied:")
        print(data.decode("utf-8"))
        client_socket.close()
    except KeyboardInterrupt:
        sys.exit(0)
