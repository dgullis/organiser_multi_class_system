class TaskList:

    # initialises empty list to store added tasks.
    def __init__(self):
        self.task_list = []
    
    # adds a task to list of tasks.
    def add_task(self, task):
        self.task_list.append(task)

    # returns list of tasks whose completed status is false.
    def see_incomplete_tasks(self):
        return [task.contents for task in self.task_list if task.completed == False]
        
    
    # returns list of tasks whose completed status is true.
    def see_completed_tasks(self):
        return [task.contents for task in self.task_list if task.completed == True]
        


