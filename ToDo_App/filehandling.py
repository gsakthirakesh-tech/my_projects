
from task_info import Task_info


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(
                f"{task.task_id}|{task.task_name}|{task.task_status}\n"
            )


def load_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_id, name, status = line.strip().split("|")

                task = Task_info(name, int(task_id), status)
                tasks.append(task)

    except FileNotFoundError:
        pass

    return tasks
