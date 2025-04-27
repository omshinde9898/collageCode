# server.py

class Server:
    def __init__(self, id):
        self.id = id
        self.request_count = 0

    def handle_request(self):
        self.request_count += 1
        print(f"--> Server-{self.id} handled request.")
