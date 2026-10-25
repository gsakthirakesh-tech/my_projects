
from task_manager import Task_manager

tm = Task_manager()

while True:
    print("---------options----------")
    print("1.add")
    print("2.display")
    print("3.view")
    print("4.update")
    print("5.update task completion")
    print("6.delete")
    print("7.end")
    print("--------End------------")

    options = input("enter a option: ")

    match options:
        case "1":
            name = input("Enter the name of the task: ")
            status = input("Enter the status (Pending/Completed): ")
            tm.add_task(name, status)

        case "2":
            tm.display()

        case "3":
            id = int(input("enter the id of the task you want to view: "))
            tm.view(id)

        case "4":
            id = int(input("enter the id of the task you want to change: "))
            tm.update(id)

        case "5":
            id = int(input("enter the id of the task you want to change: "))
            tm.update_task_completion(id)

        case "6":
            id = int(input("enter the id of the task you want to change: "))
            tm.delete_task(id)

        case "7":
            print("exiting ToDo app")
            break

        case _:
            print("Invalid option, Please try again")
