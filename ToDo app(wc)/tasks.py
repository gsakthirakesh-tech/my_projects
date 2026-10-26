tasks = []

def add_task():
    description = input("Enter task description: ")
    if description == "":
        print("Error: Task description cannot be empty!")
    else:
        if len(tasks) == 0:
            task_id = 1
        else:
            max_id = 0
            for t in tasks:
                max_id = max(max_id, t["id"])
            task_id = max_id + 1

        new_task = {
            "id": task_id,
            "description": description,
            "status": "Pending"
        }
        tasks.append(new_task)
        print("Task added successfully!")
        print("ID:", task_id)
        print("Task:", description)
        print("Status: Pending")

def view_tasks():
    print("\n--- View Tasks ---")
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for t in tasks:
            print("ID:", t["id"])
            print("Task:", t["description"])
            print("Status:", t["status"])
            print("-" * 15)

def search_task():
    print("\n--- Search Task ---")
    if len(tasks) == 0:
        print("No tasks available to search.")
    else:
        try:
            search_id = int(input("Enter task ID to search: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        
        found = False
        for t in tasks:
            if t["id"] == search_id:
                print("ID:", t["id"])
                print("Task:", t["description"])
                print("Status:", t["status"])
                print("-" * 15)
                found = True
                break
        
        if found == False:
            print("Error: Task ID not found.")

def update_task():
    print("\n--- Update Task ---")
    if len(tasks) == 0:
        print("No tasks available to update.")
    else:
        try:
            update_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        
        found = False
        for t in tasks:
            if t["id"] == update_id:
                new_desc = input("Enter new task description: ")
                if new_desc == "":
                    print("Description cannot be empty!")
                else:
                    t["description"] = new_desc
                    print("Task updated successfully!")
                found = True
                break
        
        if found == False:
            print("Error: Task ID not found.")

def complete_task():
    print("\n--- Mark Task as Completed ---")
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        try:
            complete_id = int(input("Enter task ID to mark as completed: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        
        found = False
        for t in tasks:
            if t["id"] == complete_id:
                t["status"] = "Completed"
                print("Task marked as completed successfully!")
                found = True
                break
        
        if found == False:
            print("Error: Task ID not found.")

def delete_task():
    print("\n--- Delete Task ---")
    if len(tasks) == 0:
        print("No tasks available to delete.")
    else:
        try:
            delete_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        
        found = False
        for i in range(len(tasks)):
            if tasks[i]["id"] == delete_id:
                tasks.pop(i)
                print("Task successfully deleted!")
                found = True
                break
        
        if found == False:
            print("Error: Task ID not found.")