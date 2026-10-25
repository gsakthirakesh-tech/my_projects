
from task_info import Task_info
from filehandling import save_tasks, load_tasks


class Task_manager:
  def __init__(self):
        self.store = load_tasks()
        self.next_id = 1

        if self.store:
            self.next_id = max(
                task.task_id for task in self.store
            ) + 1

  def add_task(self, name, status):
        task = Task_info(name, self.next_id, status)
        self.store.append(task)

        save_tasks(self.store)

        print(f"Task added successfully. ID: {self.next_id}")
        self.next_id += 1

  def display(self):
        if self.store:
            for task in self.store:
                task.display()
        else:
            print("No task found")

  def view(self, id):
        if self.store:
            for task in self.store:
                if task.task_id == id:
                    task.display()
                    print("The task is found")
                    return

            print(f"The task ID {id} you have given is not found")
        else:
            print("No task is found")

  def update(self, id):
        for task in self.store:
            if task.task_id == id:
                field = input(
                    "Enter what you want to update (name/status): "
                ).lower()

                match field:
                    case "name":
                        name = input("Enter the new name: ")
                        task.task_name = name

                    case "status":
                        status = input("Enter the new status: ")
                        task.task_status = status

                    case _:
                        print("The attribute you entered was not found")
                        return

                save_tasks(self.store)
                print("Task updated successfully")
                return

        print(f"The task ID {id} you have given is not found")

  def update_task_completion(self, id):
        for task in self.store:
            if task.task_id == id:
                if task.task_status.lower() == "completed":
                    print("The task is already completed")
                else:
                    task.task_status = "Completed"
                    save_tasks(self.store)
                    print("Task marked as completed")
                return

        print(f"The task ID {id} you have given is not found")

  def delete_task(self, id):
        for task in self.store:
            if task.task_id == id:
                self.store.remove(task)

                save_tasks(self.store)

                print("Task deleted successfully")
                return

        print(f"The task ID {id} you have given is not found")
