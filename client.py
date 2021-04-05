# Client

import socket
import sys

# This handles the client process
# Opens a socket, takes in the IP and payload from the command line
# Encodes it, and sends it off to the server
# If no message is received, the client times out after 5 seconds

def client_process(msg, ip_destination):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(msg.encode("utf-8"),(ip_destination, 1234))
        client_socket.settimeout(5)
        data,address=client_socket.recvfrom(4096)
        print("Server at " + str(address[0]) + ", " + str(address[1]) + " replied:")
        print(data.decode("utf-8"))
        client_socket.close()
    # This silences traceback on ctrl-break or ctrl-c
    except KeyboardInterrupt:
        sys.exit(0)
