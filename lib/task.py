class Task:

    # initialises task with specified contents.
    # sets completed status  to false.
    def __init__(self, contents):
        self.contents = contents
        self.completed = False
    
    # changes completed status to True.
    def mark_task_complete(self):
        self.completed = True