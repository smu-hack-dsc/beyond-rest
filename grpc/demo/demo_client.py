import grpc
import json  
import demo_pb2
import demo_pb2_grpc

def sendRequest(stub, message):    
    response = stub.GetServerResponse(demo_pb2.Response(message=message))
    print(response.message)
    
def sendRequestClingy(stub, message):
    responses = stub.GetMultipleServerResponse(demo_pb2.Response(message=message))
    for response in responses:
        print(response.message)

def sendRequestJSON(stub, message):
    response = stub.GetServerResponseJSON(demo_pb2.Response(message=message))
    print(response.message)         
    

def run():
    channel = grpc.insecure_channel('localhost:50051')    
    stub = demo_pb2_grpc.DemoStub(channel)
    # sendRequestClingy(stub, "Hello Server, I am Sean!")

    jsonData = json.dumps({'message': 'Hello Server, I am Sean!'})    
    sendRequestJSON(stub, jsonData)
       

if __name__ == '__main__':
    run()