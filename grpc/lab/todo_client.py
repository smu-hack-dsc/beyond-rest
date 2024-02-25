import grpc
import todo_pb2
import todo_pb2_grpc

def add_task(stub, task):
    response = stub.AddTask(todo_pb2.TaskRequest(task=task))
    print(response.message)

def get_tasks(stub):
    response = stub.GetTasks(todo_pb2.Empty())
    if len(response.tasks) == 0:
        print("There are currently no tasks")
    else:
        print("Tasks:")
        for task in response.tasks:
            print(f"- {task}")    

def delete_all_tasks(stub):
    response = stub.RemoveAllTasks(todo_pb2.Empty())
    print(response.message)

def add_multiple_tasks(stub, tasks):
    requests = (todo_pb2.TaskRequest(task=task) for task in tasks)
    response = stub.AddMultipleTasks(requests)
    print(response.message)

def get_task_history(stub):
    responses = stub.GetTaskHistory(todo_pb2.Empty())
    print("Task Updates:")
    for response in responses:
        print(response.message)


def run():
    channel = grpc.insecure_channel('localhost:50051')    
    stub = todo_pb2_grpc.TodoServiceStub(channel)
    print("1. Add task list\n2. Add multiple tasks to list\n3. Get current tasks in list\n4. Get task history\n5. Delete all tasks in TODO list\n6. End")

    while 1:        
        rpc_call = int(input("Which rpc call would you like to make: ")) 
        
        if rpc_call == 1:            
            task = str(input("What task would you like to add to the list: "))
            add_task(stub, task)
        elif rpc_call == 2:
            tasks = input("Enter tasks (comma-separated): ").split(',')
            add_multiple_tasks(stub, tasks)            
        elif rpc_call == 3:
            get_tasks(stub)            
        elif rpc_call == 4:
            get_task_history(stub)    
        elif rpc_call == 5:
            delete_all_tasks(stub)    
        else:
            print("Bye bye!")
            break

if __name__ == '__main__':
    run()