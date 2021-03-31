# Simple network sockets program using Python

# Note: UDP sockets are created using |with socket.SOCK_DGRAM|

# Main: Handles main args (Server/Client)

# Server: Receives the messages and replies with 2* the data

# Client: Takes IP address of of a host running the server process

import sys
import client
import server

def main(argv):
    if argv[0] == "client":
        if argv[1] == "home":
            ip_destination = "127.0.0.1"
        else:
            ip_destination = input("Enter the IP address to send to:\n")
        payload = input("Enter the payload string to send: \n")
        client.client_process(payload, ip_destination)
    if argv[0] == "server":
        server.server_process()

if __name__ == "__main__":
   main(sys.argv[1:])