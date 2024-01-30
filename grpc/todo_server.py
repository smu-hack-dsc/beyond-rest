# todo_server.py

import grpc
from concurrent import futures
import todo_pb2
import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServiceServicer):
    def __init__(self):
        self.tasks = []

    def AddTask(self, request, context):
        task = request.task
        self.tasks.append(task)
        return todo_pb2.TaskResponse(message=f'Task "{task}" added successfully.')

    def GetTasks(self, request, context):
        return todo_pb2.TasksList(tasks=self.tasks)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    print('Server started on port 50051...')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
