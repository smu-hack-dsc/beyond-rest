"""
TO COMPILE PROTOCOL BUFFERS (PROTOBUF) FILE INTO PYTHON CODE FOR gRPC   

python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. todo.proto

1. -m grpc_tools.protoc => Invokes Protocol Buffers compiler (protoc) using grpc_tools.protoc (Python module) 
2. -I .                 => Specifies dir to search for imported .proto files. (.) indicates search current dir for imports 
3. --python_out=.       => Specifies dir where generated python code should be placed. (.) sets it to curr dir 
4. --grpc_python_out=.  => Specifies dir where generated gRPC python code should be placed. (.) sets to curr dir 
5. todo.proto           => Specific Protocol Buffers file user wants to compile
"""

import grpc
from concurrent import futures
import todo_pb2
import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServiceServicer):
    def __init__(self, *args, **kwargs):
        self.tasks = []

    def AddTask(self, request, context):
        task = request.task
        self.tasks.append(task)
        return todo_pb2.TaskResponse(message=f'Task "{task}" added successfully.')

    def GetTasks(self, request, context):
        return todo_pb2.TasksList(tasks=self.tasks)

    def RemoveAllTasks(self, request, context):
        self.tasks = []
        return todo_pb2.TaskResponse(message=f'All tasks deleted')
    
    def AddMultipleTasks(self, request_iterator, context):
        added_tasks = []
        for request in request_iterator:
            task = request.task
            self.tasks.append(task)
            added_tasks.append(task)
        return todo_pb2.TaskResponse(message=f'Tasks {added_tasks} added successfully.')
    
    def GetTaskHistory(self, request, context):
        for index, task in enumerate(self.tasks):
            yield todo_pb2.TaskResponse(message=f'Task {index+1} added: {task}')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    print('Server started on port 50051...')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
