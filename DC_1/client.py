import xmlrpc.client

# Connect to server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
n = int(input("Enter an integer to calculate factorial: "))

# Remote function call
result = server.factorial(n)

print(f"The factorial of {n} is {result}")
