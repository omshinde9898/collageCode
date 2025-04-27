# main.py

from server import Server
from load_balancer import LoadBalancer
from client import Client

def main():
    # Create 3 servers
    servers = [Server(i+1) for i in range(3)]
    lb = LoadBalancer(servers)
    client = Client(lb)

    # Simulate 10 client requests
    for i in range(10):
        print(f"\nRequest #{i+1}")
        client.send_request()

if __name__ == "__main__":
    main()
