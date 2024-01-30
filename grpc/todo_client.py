# todo_client.py

import grpc
import todo_pb2
import todo_pb2_grpc

def add_task(stub, task):
    response = stub.AddTask(todo_pb2.TaskRequest(task=task))
    print(response.message)

def get_tasks(stub):
    response = stub.GetTasks(todo_pb2.Empty())
    print("Tasks:")
    for task in response.tasks:
        print(f"- {task}")

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TodoServiceStub(channel)

    # Add tasks
    add_task(stub, "Buy groceries")
    add_task(stub, "Finish project")

    # Get tasks
    get_tasks(stub)

if __name__ == '__main__':
    run()
