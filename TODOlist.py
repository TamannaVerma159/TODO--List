#TODO List
tasks = []
def display_task():
    print("Hello Tamanna!   ")
    print("1. Add task")
    print("2. View tasks")
    print("3. MArk task")
    print("4. delete task")
    print("5. Exit")

def Addtask():
    task = input("Enter your task:-  ")
    tasks.append({"discription":task, "completed": False})
    print("Task Added")
def Viewtask():
    if not tasks:
        print("No task mentioned yet!")
        return
    for i , task in enumerate(tasks):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{i+1}. {status} {task['discription']}")
def markTask():
    donetask = input("Enter the task you done! ")
    for task in tasks:
        if task["discription"] == donetask:
            task ["completed"] = True
            print("Task marked as completed!")
            return
def deletetask():
    delete = input("Which task you want to delete: ")
    for task in tasks:
        if task["discription"] == delete:
            
            tasks.remove(task)
            print("task is deleted")
            return
    else:
        print("your task is not in the list")

while True:
    display_task()
    choice=input("Enter your choice what you want to do: ")

    if choice=="1":
        Addtask()
    elif choice=="2":
        Viewtask()
    elif choice=="3":
        markTask()    
    elif choice=="4":
        deletetask()    
    elif choice=="5":
        print("Exiting from TO-DO List. Good Bye!")    
        break
    else:
        print("Invalid input! Please enter from the above choices ")

