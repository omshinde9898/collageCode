import grpc
import factorial_pb2
import factorial_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = factorial_pb2_grpc.FactorialServiceStub(channel)
        
        while True:
            user_input = input("Enter a positive integer to calculate factorial: ").strip()
            
            if not user_input.isdigit():
                print("❌ Invalid input. Please enter a valid positive integer.")
                continue
            
            number = int(user_input)
            response = stub.ComputeFactorial(factorial_pb2.FactorialRequest(number=number))
            print(f"✅ Factorial of {number} is: {response.result}")
            continue  # Remove this if you want to allow multiple inputs

if __name__ == '__main__':
    run()
