# Simple network sockets program using Python

# Main: Handles main args (Server/Client)

import sys
import client
import server

# This handles the command line arguments, and runs the appropriate process

def main(argv):
    if argv[0] == "client":
        if len(argv) == 1:
            ip_destination = input("No IP specified, please enter:")
            print(ip_destination)
        if len(argv) == 2:
            if argv[1] == "localhost":
                ip_destination = "127.0.0.1"
            ip_destination = argv[1] 
        payload = input("Enter the payload string to send: \n")
        client.client_process(payload, ip_destination)
    if argv[0] == "server":
        server.server_process()

if __name__ == "__main__":
   main(sys.argv[1:])
