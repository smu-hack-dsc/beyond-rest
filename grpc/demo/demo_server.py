# python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. demo.proto

import grpc
import json 
from concurrent import futures
import demo_pb2  
import demo_pb2_grpc

class DemoService(demo_pb2_grpc.DemoServicer):
    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        msgRequest = request.message
        result = f"Server is up and running, received your message: {msgRequest}"
        return demo_pb2.Response(message=result)

    def GetMultipleServerResponse(self, request, context):
        msgRequest = request.message
        result = f"Server is up and running, received your message: {msgRequest}"
        for _ in range(10):
            yield demo_pb2.Response(message=result)

    def GetServerResponseJSON(self, request, context):
        json_data = json.loads(request.message)
        message = demo_pb2.Request(message=json_data['message'])
        response = self.GetServerResponse(message, context)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DemoServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:50051')
    print('Server started on port 50051...')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()