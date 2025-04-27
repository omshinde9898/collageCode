import grpc
from concurrent import futures
import time
import factorial_pb2
import factorial_pb2_grpc

class FactorialServicer(factorial_pb2_grpc.FactorialServiceServicer):
    def ComputeFactorial(self, request, context):
        n = request.number
        result = 1
        for i in range(2, n + 1):
            result *= i
        return factorial_pb2.FactorialResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    factorial_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    try:
        while True:
            time.sleep(86400)  # Sleep for 1 day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
