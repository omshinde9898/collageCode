from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is listening on port 8000...")

# Register function
server.register_function(factorial, "factorial")

# Run server
server.serve_forever()
