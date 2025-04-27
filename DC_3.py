import random
import time
import threading

# Server class to simulate the processing of requests
class Server:
    def __init__(self, name):
        self.name = name
        self.connections = 0  # Number of active connections (requests)

    def handle_request(self):
        """Simulate handling a request by increasing active connections."""
        self.connections += 1
        print(f"{self.name} is handling the request. Active connections: {self.connections}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate the processing time
        self.connections -= 1
        print(f"{self.name} has finished handling the request. Active connections: {self.connections}")

# Load Balancer class to simulate distributing requests among servers
class LoadBalancer:
    def __init__(self, servers, algorithm='round_robin'):
        self.servers = servers
        self.algorithm = algorithm
        self.round_robin_index = 0  # Used for Round Robin algorithm

    def distribute_request(self, client_id):
        """Distribute requests based on the selected algorithm."""
        if self.algorithm == 'round_robin':
            return self.round_robin(client_id)
        elif self.algorithm == 'least_connections':
            return self.least_connections(client_id)

    def round_robin(self, client_id):
        """Round Robin algorithm: distribute requests in a circular manner."""
        server = self.servers[self.round_robin_index]
        self.round_robin_index = (self.round_robin_index + 1) % len(self.servers)
        print(f"Client {client_id} is sending a request to {server.name} (Round Robin)")
        server.handle_request()
        return server

    def least_connections(self, client_id):
        """Least Connections algorithm: send the request to the server with the least active connections."""
        server = min(self.servers, key=lambda s: s.connections)
        print(f"Client {client_id} is sending a request to {server.name} (Least Connections)")
        server.handle_request()
        return server

# Simulate client requests
def simulate_client_requests(client_id, load_balancer):
    """Simulate a client sending multiple requests."""
    for _ in range(random.randint(3, 5)):  # Each client sends 3-5 requests
        load_balancer.distribute_request(client_id)
        time.sleep(random.uniform(1, 3))  # Wait before sending the next request

# Main simulation function
def main():
    # Create some server instances
    servers = [Server(f"Server {i+1}") for i in range(3)]  # 3 servers

    # Choose the load balancing algorithm
    lb_algorithm = 'least_connections'  # You can switch this to 'round_robin' to test other algorithm
    load_balancer = LoadBalancer(servers, lb_algorithm)

    # Simulate multiple client requests
    clients = [threading.Thread(target=simulate_client_requests, args=(i+1, load_balancer)) for i in range(5)]  # 5 clients

    # Start all client threads
    for client in clients:
        client.start()

    # Wait for all client threads to finish
    for client in clients:
        client.join()

if __name__ == "__main__":
    main()
