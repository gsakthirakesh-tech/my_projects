class Task_info:
  def __init__(self,task_name,task_id,task_status):
    self.task_name=task_name
    self.task_id=task_id
    self.task_status=task_status



  def display(self):
    print(f"task_name:{self.task_name}")
    print(f"task_id:{self.task_id}")
    print(f"task_status:{self.task_status}")



    