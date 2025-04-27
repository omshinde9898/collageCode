# client.py

class Client:
    def __init__(self, load_balancer):
        self.load_balancer = load_balancer

    def send_request(self):
        print("Client sending a request...")
        server = self.load_balancer.get_next_server()  # Correct method
        server.handle_request()
